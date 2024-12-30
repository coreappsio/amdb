# Avalanche Metadata Database

<p align="center">

<p align="center">
<img align="center" width="150px" height="auto" src="./amdb.svg">
</p>
  <p align="center">
An open-source repository providing structured metadata for Avalanche L1s to enable seamless discovery and integration

</p>

## Table of Contents

- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Metadata Schema](#metadata-schema)
- [Key Features](#key-features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

The Avalanche Metadata Database (AMDB) is a comprehensive and flexible repository designed to provide structured and accessible metadata for Avalanche L1s. It serves as a unified resource for storing and sharing critical network information, enabling seamless discovery and integration across the Avalanche ecosystem.

AMDB supports both Fuji (testnet) and Mainnet, offering developers, researchers, and explorers a standardized schema for retrieving detailed metadata. This repository was established as a **public good**, ensuring free and open access to off-chain data while fostering collaboration within the Avalanche community.

While Snowpeer initially developed and maintains AMDB, it is designed to be **community-driven**. Contributions are encouraged, allowing others to extend its capabilities and improve its contents collaboratively.

## Folder Structure

```
├── amdb/
│   ├── fuji/
│   │   └── l1s/
│   ├── mainnet/
│   │   └── l1s/
│   │       ├── example-l1/
│   │       │   ├── example-l1.json
│   │       │   └── assets/
│   │       │       └── logo.png
```

- **fuji/l1s**: Contains metadata for Avalanche L1s deployed on the Fuji testnet.
- **mainnet/l1s**: Contains metadata for Avalanche L1s deployed on the Avalanche Mainnet.
- **example-l1**: Example structure for an Avalanche L1, including a JSON metadata file and assets like logos.

## Metadata Schema

The AMDB schema is designed to store comprehensive metadata for Avalanche L1s, including details about their configurations and assets. Below is the schema structure:

```javascript
{
    id: "", // ID of Avalanche L1 (mandatory)
    name: "", // Name of the l1
    description: "", // Brief description 
    logo: "", // URL or path to the l1's logo
    primaryColor: "", // Primary branding color
    permissionless: true,
    private: false,
    chains: [
        {
            id: "", // Blockchain ID for the chain
            name: "", // Name of the chain
            description: "", // Description of the chain
            evmId: "", // EVM identifier
            vmID:"",
            vmName: "", // Virtual Machine name
            explorerUrl: "", // URL to the chain explorer
            rpcUrl: "", // URL for RPC endpoint
            assets: [
                {
                    name: "", // Asset name
                    symbol: "", // Asset symbol
                    type: "GAS | GOVERNANCE | ETC.", // Asset type
                    denomination: "", // Denomination details
                    cap: "FIXED | UNLIMITED", // Supply cap type 
                    description: "", // Description of the asset
                    logo: "", // URL to the asset logo
                    pricingDataProvider: [
                        {
                            name: "CoinGecko", // Pricing provider
                            id: "" // Provider-specific identifier
                        },
                        {
                            name: "CoinMarketCap", // Alternative provider
                            id: ""
                        }
                    ]
                }
            ]
        }
    ],
    links: {
        website: "", // Official website URL
        whitepaper: "", // Whitepaper URL
        explorers: [
            "" // List of block explorer URLs
        ],
        forum: "", // Community forum link
        git: "", // Git repository link
        docs: "", // Documentation link
        socials: [
            {
                name: "", // Social media platform
                url: "" // URL to profile
            }
        ]
    },
    team: [
        {
            name: "", // Team member's name
            role: "", // Role within the team
            socials: [
                {
                    name: "", // Social media platform
                    url: "" // URL to profile
                }
            ]
        }
    ],
    mainCategory: "", // Primary category of the network
    categories: [
        "" // Additional categories
    ]
}
```

## Key Features

- **Modular Structure**: Supports metadata for multiple Avalanche L1s and chains.
- **Scalable Design**: Can be extended to include additional metadata fields as required.
- **Dynamic API Integration**: Allows integration with pricing data providers like CoinGecko and CoinMarketCap.
- **Rich Metadata**: Captures detailed information about assets, including type, denomination, and supply cap.
- **Links and Socials**: Provides connectivity to official websites, whitepapers, explorers, and social channels.

## Contributing

Contributions are welcome! If you want to add or modify metadata, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Ensure your updates follow the schema guidelines.
4. Submit a pull request.

For major changes, please open an issue first to discuss what you would like to implement.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For inquiries or support, please reach out via [GitHub Issues](https://github.com/your-repo/amdb/issues) or contact the team directly through our listed social channels.
