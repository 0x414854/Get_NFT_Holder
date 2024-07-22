![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Get NFT Holder

## **Description**
**This Python project retrieves and saves data about NFT holders from various blockchain networks.**
<br>The script collects information about the owners of specific NFT collections and **updates the data every 5 minutes**.
<br>The retrieved data is saved in both **JSON** and **CSV** formats.



## **Features**
- **Multi-Network Compatibility** : Supports 6 different blockchain networks: `Ethereum`, `Polygon`, `Arbitrum`, `Optimism`, `Base` and `Starknet`.
- **Periodic Updates** : Fetches and updates NFT holder data every 5 minutes.
- **Data Storage** : Saves data in JSON and CSV formats, including details about NFT owners and their balances.
- **Automatic Directory Management** : Creates and manages directories to store the fetched data, ensuring that the latest data is always available.

## **Supported Networks**
- **Ethereum Mainnet** (`eth-mainnet`)
- **Polygon Mainnet** (`polygon-mainnet`)
- **Arbitrum Mainnet** (`arb-mainnet`)
- **Optimism Mainnet** (`opt-mainnet`)
- **Base Mainnet** (`base-mainnet`)
- **Starknet Mainnet** (`starknet-mainnet`)

## **Collections Infos** (example)
- **`Pudgy_Penguins` : `0xBd3531dA5CF5857e7CfAA92426877b022e612cf8`**
- **`Lil_Pudgy` : `0x524cAB2ec69124574082676e6F654a18df49A048`**
- **`Bored_Ape_Yacht_Club` : `0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D`**


## **Prerequisites**
- **`Python 3.x`** installed on your machine
- **`Requests`** library
- **`Schedule`** library
- **`ShadePy`** library 

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the install command.

1. Clone this repository to your machine.

    ```bash
    git clone https://github.com/0x414854/Get_NFT_Holder.git

2. Install the required libraries.

    ```bash
    pip install requests schedule shadePy

3. Replace `YOUR_API_KEY` in the script with your actual [Alchemy](https://www.alchemy.com) API key.

    ```python
    API_KEY = "YOUR_API_KEY"

4. Customize the `NETWORK`, `COLLECTION_NAME` and `CONTRACT_ADDRESS` variables in the script based on the collection and network you want to query.

   ```python
    NETWORK = "eth-mainnet"
    CONTRACT_ADDRESS = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8"
    COLLECTION_NAME = "Pudgy_Penguins"

5. Once the installation is complete, you're ready to run the program!

   ```bash
   python3 get_NFT_holder.py  

## **Usage Examples**
- Run the Python script.
- The script will start fetching data from the specified network and NFT contract address every 5 minutes.
- The data will be saved in the "Pudgy_Penguins" directory (or the directory corresponding to the collection name) in both JSON and CSV formats.
- The console will display messages indicating whether the data is up-to-date or if there was an error fetching the data.


## Tree Directory

Get_NFT_Holder/
<br>├── get_NFT_holder.py
<br>└── README.md

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)
