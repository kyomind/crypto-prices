import csv
import os
from datetime import datetime

from pycoingecko import CoinGeckoAPI

client = CoinGeckoAPI()
btc = client.get_price(ids='bitcoin', vs_currencies='usd')
print(btc)


def store_coin_list():
    coin_list = client.get_coins_list()
    with open('coin_list.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'symbol', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(coin_list)


if __name__ == "__main__":
    # 檔案不存在時建立
    if not os.path.isfile('coin_list.csv'):
        store_coin_list()
