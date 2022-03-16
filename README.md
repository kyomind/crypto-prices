# Crypto Prices
使用 CoinGecko Python SDK (API) 取得指定加密貨幣報價並寫入自己的 Google Sheets 裡，方便後續製作專屬的 Portfolio

## Main Pacakges
- [pycoingecko](https://github.com/man-c/pycoingecko)
- [pygsheets](https://github.com/nithinmurali/pygsheets)


## Dev Log
`2022/03/15`
- 建立開發環境，使用 [Poetry](https://python-poetry.org/)
- 將所有支援的加密貨幣清單以`csv`格式存到本機，作為對照表

`2022/03/16`
- 以 Python configparser 建立並讀自己的coin清單
- 建立`config.ini`