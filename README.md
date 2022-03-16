# Crypto Prices
使用 CoinGecko Python SDK (API) 取得指定加密貨幣報價並寫入自己的 Google Sheets 裡，方便後續製作專屬的 Portfolio

## Main pacakges
- [pycoingecko](https://github.com/man-c/pycoingecko)
- [pygsheets](https://github.com/nithinmurali/pygsheets)


## Dev logs
`2022/03/15`
- 建立開發環境，使用 [Poetry](https://python-poetry.org/)
- 將 CoinGecko 所有支援的加密貨幣以`csv`清單格式存到本機，作為快取對照表，以取得 coin 的 symbol，比如 BTC、ETH（預設使用 id　查詢），清單內容也可參見 [API 說明](https://www.coingecko.com/en/api/documentation)

`2022/03/16`
- 以 Python configparser 標準庫建立並讀自己的追縱　coin　清單
- 建立`config.ini`
- coin 決定以「`,`」分隔，而不採用原先的空白分隔，因為和 API 的參數格式（id of coins, comma-separated if querying more than 1 coin
）較為一致