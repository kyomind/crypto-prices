import csv
import os
from configparser import ConfigParser
from datetime import datetime

from pycoingecko import CoinGeckoAPI

config = ConfigParser()
config.read('config.ini')
coin_gecko = CoinGeckoAPI()


def store_coin_list():
    coin_list = coin_gecko.get_coins_list()
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
    res = coin_gecko.get_price(ids=coin_ids, vs_currencies='usd')
    print(res)
