import csv
import os
from configparser import ConfigParser

import gspread
from pycoingecko import CoinGeckoAPI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'coins.csv')

config = ConfigParser()
config_path = os.path.join(BASE_DIR, 'config.ini')
config.read(config_path)
coin_client = CoinGeckoAPI()


def create_id_symbol_mapping():
    with open(csv_path) as csv_file:
        coins = csv.DictReader(csv_file)
        return {coin['id']: coin['symbol'].upper() for coin in coins}


def get_worksheet():
    key_path = os.path.join(BASE_DIR, 'key.json')
    sheet_client = gspread.service_account(key_path)
    sheet_name = config['my_coin_config']['google_sheet_name']
    return sheet_client.open(sheet_name).sheet1


def store_coins_csv():
    coins = coin_client.get_coins_list()
    with open(csv_path, 'w', newline='') as csv_file:
        fieldnames = ['id', 'symbol', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(coins)


def get_my_coin_ids() -> str:
    coin_ids: str = config['my_coin_config']['coin_ids']
    coin_ids = coin_ids.replace(' ', '').replace('\n', '')
    return coin_ids


def convert_api_response_to_sheet_rows(api_response: dict, coin_ids: str) -> list:
    id_symbol_mapping = create_id_symbol_mapping()
    sheet_rows = []
    for coin_id in coin_ids.split(','):
        if not coin_id:
            raise ValueError('config coin_ids 格式有誤')
        if coin_id not in id_symbol_mapping:
            raise ValueError(f'coin id="{coin_id}" 不存在')
        coin_symbol = id_symbol_mapping[coin_id]
        coin_price = api_response[coin_id]['usd']
        sheet_rows.append([coin_symbol, coin_price])
    return sheet_rows


if __name__ == "__main__":
    # 檔案不存在時建立
    if not os.path.isfile(csv_path):
        store_coins_csv()

    my_coin_ids = get_my_coin_ids()
    response = coin_client.get_price(ids=my_coin_ids, vs_currencies='usd')
    sheet_rows = convert_api_response_to_sheet_rows(response, my_coin_ids)

    sheet = get_worksheet()
    sheet.update(f'A2:B{len(sheet_rows)+1}', sheet_rows)
