import csv
import os
from configparser import ConfigParser

import gspread
from pycoingecko import CoinGeckoAPI

config = ConfigParser()
config.read('config.ini')
coin_client = CoinGeckoAPI()


def create_id_symbol_mapping():
    with open('coins.csv') as csv_file:
        coins = csv.DictReader(csv_file)
        return {coin['id']: coin['symbol'].upper() for coin in coins}


def get_worksheet():
    sheet_client = gspread.service_account(filename='key.json')
    return sheet_client.open("Crypto Prices").sheet1


def store_coins_csv():
    coins = coin_client.get_coins_list()
    with open('coins.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'symbol', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(coins)


def get_my_coin_ids() -> str:
    coin_ids: str = config['my_coins']['coin_ids']
    coin_ids = coin_ids.replace(' ', '').replace('\n', '')
    return coin_ids


def convert_api_response_to_sheet_rows(api_response: dict) -> list:
    id_to_symbol = create_id_symbol_mapping()
    sheet_rows = []
    for coin_id, coin_price in api_response.items():
        row = [id_to_symbol[coin_id], coin_price['usd']]
        sheet_rows.append(row)
    return sheet_rows


if __name__ == "__main__":
    # 檔案不存在時建立
    if not os.path.isfile('coins.csv'):
        store_coins_csv()

    my_coin_ids = get_my_coin_ids()
    respsone = coin_client.get_price(ids=my_coin_ids, vs_currencies='usd')
    sheet_rows = convert_api_response_to_sheet_rows(respsone)

    sheet = get_worksheet()
    sheet.update(f'A2:B{len(sheet_rows)+1}', sheet_rows)
