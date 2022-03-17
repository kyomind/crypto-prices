import csv
import os
from configparser import ConfigParser
from datetime import datetime

import gspread
from pycoingecko import CoinGeckoAPI

SHEET_URL = 'https://docs.google.com/spreadsheets/d/1WSZ8ckqIBPQA5V4FbUnfpisRhusd_WIvYGpgzKdCwak/'

config = ConfigParser()
config.read('config.ini')
coin_client = CoinGeckoAPI()


def get_worksheet():
    sheet_client = gspread.service_account(filename='key.json')
    return sheet_client.open("Crypto Prices").sheet1



def store_coin_list():
    coin_list = coin_client.get_coins_list()
    with open('coin_list.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'symbol', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(coin_list)


def get_my_coin_ids():
    coin_ids = config['my_coin_list']['coin_ids']
    return coin_ids


if __name__ == "__main__":
    # 檔案不存在時建立
    if not os.path.isfile('coin_list.csv'):
        store_coin_list()

    coin_ids = get_my_coin_ids()
    res = coin_client.get_price(ids=coin_ids, vs_currencies='usd')
    print(res)
    sheet = get_worksheet()
    sheet.update('A1:B2', [[1, 2], [3, 4]])
