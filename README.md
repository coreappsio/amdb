# Avalanche Network JSON Configuration

This repository contains JSON configuration files for subnets on the Avalanche network. Each JSON file includes detailed information about a specific subnet, such as its ID, name, description, icon, color, website, chains, categories, documentation, explorer, social media links, main category, and assets.

## JSON File Structure

Each JSON file should follow the structure shown below:

```json
{
  "id": "11111111111111111111111111111111LpoYY",
  "name": "Avalanche Primary Network",
  "description": "Avalanche is the fastest smart contracts platform in the blockchain industry, as measured by time-to-finality. Avalanche is blazingly fast, low cost, and eco-friendly",
  "icon": "https://cdn.snowpeer.io/avax.svg",
  "color": "#f34333",
  "website": "https://avax.network",
  "chains": [
    {
      "name": "C-Chain",
      "id": "2"
    },
    {
      "name": "X-Chain",
      "id": "3"
    }
  ],
  "categories": [
    "L1",
    "Smart Contracts"
  ],
  "docs": "https://docs.avax.network",
  "explorer": "https://explorer.avax.network",
  "socials": [
    {
      "name": "Twitter",
      "url": "https://twitter.com/avalancheavax"
    },
    {
      "name": "Reddit",
      "url": "https://reddit.com/r/avax"
    }
  ],
  "mainCategory": "Blockchain",
  "assets": [
    {
      "for": "AVAX",
      "pricingDataProvider": [
        {
          "name": "CoinGecko",
          "id": "avalanche-2"
        },
        {
          "name": "CoinMarketCap",
          "id": "avax"
        }
      ],
      "symbol": "AVAX",
      "name": "Avalanche"
    }
  ]
}


Adding New Subnets
To add a new subnet to the system, follow these steps:

1-Fork the Repository: Create a fork of this repository on GitHub.
2-Create a JSON File: Create a new JSON file with the structure shown above and fill in the necessary details for your subnet.
3-Place the JSON File: Place the JSON file in the appropriate directory (fuji/l1s or mainnet/l1s).
4-Commit and Push: Commit your changes and push them to your forked repository.
5-Create a Pull Request: Open a pull request to the original repository to integrate your subnet into the system.

Updating an Existing Subnet

To update an existing subnet, follow these steps:

1-Fork the Repository: Create a fork of this repository on GitHub.
2-Find the JSON File: Locate the JSON file you want to update and make the necessary changes.
3-Commit and Push: Commit your changes and push them to your forked repository.
4-Create a Pull Request: Open a pull request to the original repository to integrate your changes.

Contributing
We welcome contributions! Whether you are adding new subnets or updating existing ones, please follow the steps outlined above. If you have any questions or suggestions, feel free to open an issue.

License
This project is licensed under the MIT License. For more information, see the LICENSE file.