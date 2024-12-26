# Avalanche Metadata DB

This project aims to standardize subnet/L1 metadata on the Avalanche network. It includes information like name, website, and price data from APIs (e.g., CoinGecko). This data is accessible via the Snowpeer API for explorers and researchers.

## Project Structure

- **fuji/l1s**: JSON files for the Fuji testnet.
- **mainnet/l1s**: JSON files for the Mainnet.

## L1 Model Sample

```json
{
  "id": "",
  "name": "",
  "description": "",
  "logo": "",
  "primaryColor": "",
  "permissionless": true,
  "private": false,
  "chains": [
    {
      "id": "",
      "name": "",
      "description": "",
      "evmId": "",
      "vmName": "",
      "explorerUrl": "",
      "rpcUrl": "",
      "assets": [
        {
          "name": "",
          "symbol": "",
          "type": "",
          "denomination": "",
          "cap":  "",
          "description": "",
          "logo": "",
          "pricingDataProvider": [
            {
              "name": "CoinGecko",
              "id": ""
            },
            {
              "name": "CoinMarketCap",
              "id": ""
            }
          ]
        }
      ]
    }
  ],
  "links": {
    "website": "",
    "whitepaper": "",
    "forum": "",
    "git": "",
    "docs": "",
    "socials": [
      {
        "name": "",
        "url": ""
      }
    ]
  },
  "team": [
    {
      "name": "",
      "role": "",
      "socials": [
        {
          "name": "",
          "url": ""
        }
      ]
    }
  ],
  "mainCategory": "",
  "categories": [
    ""
  ]
}
```

## Contributing

1. Fork the repository.
2. Clone your fork:
  ```sh
  git clone https://github.com/your-username/amdb.git
  ```
3. Create a new branch:
  ```sh
  git checkout -b your-branch-name
  ```
4. Make your changes.
5. Commit your changes:
  ```sh
  git add .
  git commit -m "Description of your changes"
  ```
6. Push to your fork:
  ```sh
  git push origin your-branch-name
  ```
7. Create a Pull Request.

## Code of Conduct

This project follows a [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file.
