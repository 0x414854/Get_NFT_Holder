import os
import requests
import schedule
import json
from datetime import datetime
from shadePy import Colors

RED = Colors.RED
GREEN = Colors.GREEN
YELLOW = Colors.YELLOW
RESET = Colors.RESET

NETWORK = "eth-mainnet"
CONTRACT_ADDRESS = "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8"
COLLECTION_NAME = "Pudgy_Penguins"
API_KEY = "YOUR_API_KEY"
WITH_TOKEN_BALANCE = True 
CHECK_INTERVAL = 5

def get_nft_holder():
    url = f"https://{NETWORK}.g.alchemy.com/nft/v2/{API_KEY}/getOwnersForContract?contractAddress={CONTRACT_ADDRESS}&withTokenBalances={WITH_TOKEN_BALANCE}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        new_data = response.json()
        owner_addresses = new_data.get("ownerAddresses", [])
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = os.path.join(os.getcwd(), COLLECTION_NAME)
        os.makedirs(folder_path, exist_ok=True)

        new_txt_data = json.dumps(new_data, indent=4)
        new_csv_data = generate_csv_data(owner_addresses)

        existing_txt_path = get_latest_file(folder_path, f"{COLLECTION_NAME}_Owner_NFT_")
        existing_csv_path = get_latest_file(folder_path, f"{COLLECTION_NAME}_Owners_nft_totals_")

        if existing_txt_path and existing_csv_path:
            try:
                with open(existing_txt_path, "r", encoding="utf-8") as file:
                    existing_txt_data = file.read().strip()

                with open(existing_csv_path, "r", encoding="utf-8") as file:
                    existing_csv_data = file.read().strip()

                if existing_txt_data == new_txt_data and existing_csv_data == new_csv_data:
                    print(f"{GREEN}Data is already up-to-date{RESET} at {current_datetime}.")
                    return
            except FileNotFoundError:
                pass

        save_holders(folder_path, current_datetime, new_txt_data, new_csv_data)
    else:
        print(f"{RED}ERROR: HTTP Error: {response.status_code}{RESET}")

def generate_csv_data(owner_addresses):
    reverse_sort = True
    csv_data = "Owner Address,Total NFT Count,NFTS Hold\n"
    sorted_owner_data = sorted(owner_addresses, key=lambda x: sum(b["balance"] for b in x.get("tokenBalances", [])), reverse=reverse_sort)
    for owner_data in sorted_owner_data:
        owner_address = owner_data["ownerAddress"]
        token_balances = owner_data.get("tokenBalances", [])
        total_tokens = sum(balance["balance"] for balance in token_balances)
        nft_list = [f"#{int(balance_info['tokenId'], 16)}" for balance_info in token_balances]
        csv_data += f"{owner_address},{total_tokens},{nft_list}\n"
    return csv_data.strip()

def get_latest_file(folder_path, prefix):
    try:
        files = [f for f in os.listdir(folder_path) if f.startswith(prefix)]
        if not files:
            return None
        latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        return os.path.join(folder_path, latest_file)
    except OSError as e:
        print(f"{RED}ERROR: Error accessing files in {folder_path}: {e}{RESET}")
        return None

def save_holders(folder_path, current_datetime, txt_data, csv_data):
    txt_file_path = os.path.join(folder_path, f"{COLLECTION_NAME}_Owner_NFT_{current_datetime}.txt")
    csv_file_path = os.path.join(folder_path, f"{COLLECTION_NAME}_Owners_nft_totals_{current_datetime}.csv")

    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(txt_data)
        print(f"{GREEN}SUCCESS{RESET}: Data has been saved in '{txt_file_path}'.")

    with open(csv_file_path, "w", encoding="utf-8", newline="") as csv_file:
        csv_file.write(csv_data)
        print(f"{GREEN}SUCCESS{RESET}: Results have been saved in '{csv_file_path}'.")

def main():
    get_nft_holder()
    schedule.every(CHECK_INTERVAL).minutes.do(get_nft_holder)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()
