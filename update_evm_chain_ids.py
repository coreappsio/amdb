#!/usr/bin/env python3
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CHAINSDATA_PATH = ROOT / "chainsdata.json"
L1S_DIR = ROOT / "mainnet" / "l1s"


def load_chainsdata(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    # Build lookup by (subnetId, blockchainId) -> evmChainId
    lookup = {}
    # Also build subnetId -> list of (blockchainId, evmChainId) to create minimal chains[] when missing
    subnet_to_entries = {}
    for c in data.get("chains", []):
        subnet_id = c.get("subnetId")
        blockchain_id = c.get("blockchainId")
        evm_chain_id = c.get("evmChainId")
        if not subnet_id or not blockchain_id or evm_chain_id is None:
            continue
        lookup[(subnet_id, blockchain_id)] = evm_chain_id
        entries = subnet_to_entries.setdefault(subnet_id, [])
        entries.append((blockchain_id, evm_chain_id))
    return lookup, subnet_to_entries


def process_l1_file(path: Path, lookup: dict, subnet_to_entries: dict, dry_run: bool = False) -> bool:
    """
    Returns True if a change would be made/made.
    """
    with path.open("r", encoding="utf-8") as f:
        doc = json.load(f)

    subnet_id = doc.get("id")
    chains = doc.get("chains") or []
    changed = False

    # Remove any root-level evmChainId if present
    if "evmChainId" in doc:
        del doc["evmChainId"]
        changed = True

    for chain in chains:
        blockchain_id = chain.get("id")
        if blockchain_id is None:
            continue

        key = (subnet_id, blockchain_id)
        evm_chain_id = lookup.get(key)
        if evm_chain_id is None:
            continue

        # Only add if missing or different
        if chain.get("evmChainId") != evm_chain_id:
            chain["evmChainId"] = evm_chain_id
            changed = True

    # If there are no chains, create minimal chains[] from chainsdata matches for this subnet
    if (not chains) and subnet_id:
        entries = subnet_to_entries.get(subnet_id) or []
        if entries:
            doc["chains"] = [{"id": bid, "evmChainId": evid} for (bid, evid) in entries]
            changed = True

    if changed and not dry_run:
        # Keep formatting compact with 2 spaces and sorted keys disabled to preserve semantics
        with path.open("w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
            f.write("\n")

    return changed


def main():
    dry_run = "--dry-run" in sys.argv

    if not CHAINSDATA_PATH.exists():
        print(f"chainsdata.json not found at {CHAINSDATA_PATH}", file=sys.stderr)
        sys.exit(1)

    if not L1S_DIR.exists():
        print(f"L1 directory not found at {L1S_DIR}", file=sys.stderr)
        sys.exit(1)

    lookup, subnet_to_entries = load_chainsdata(CHAINSDATA_PATH)

    total_files = 0
    updated_files = 0
    for json_path in L1S_DIR.rglob("*.json"):
        total_files += 1
        try:
            changed = process_l1_file(json_path, lookup, subnet_to_entries, dry_run=dry_run)
        except json.JSONDecodeError as e:
            print(f"Skipping invalid JSON: {json_path}: {e}")
            continue
        if changed:
            updated_files += 1
            action = "Would update" if dry_run else "Updated"
            print(f"{action}: {json_path}")

    print(f"Processed {total_files} files. {'Would update' if dry_run else 'Updated'} {updated_files}.")


if __name__ == "__main__":
    main()


