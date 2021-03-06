# Crypto Prices
透過 CoinGecko API 取得指定加密貨幣即時報價並寫入自己的 Google Sheets 裡，供後續製作專屬的 Portfolio

![](image/demo.png)

## Main pacakges
- [pycoingecko](https://github.com/man-c/pycoingecko)
- [gspread](https://github.com/burnash/gspread)
  - ❌ [pygsheets](https://github.com/nithinmurali/pygsheets)
- [poetry](https://python-poetry.org/)
  - 套件依賴管理
  - 虛擬環境建立


## Devlogs
`2022/03/15`
- 建立開發環境，使用 [Poetry](https://python-poetry.org/)
- 將 CoinGecko 所有支援的加密貨幣以`csv`清單格式存到本機，作為快取對照表，以取得 coin 的 symbol 比如 BTC、ETH（預設使用 id 查詢）。清單內容也可參見 [API 說明](https://www.coingecko.com/en/api/documentation)

`2022/03/16`
- 以 Python 標準庫——configparser 建立並讀自己的追縱 coin 清單
- 建立`config.ini`
- coin 決定以「`,`」分隔，而不採用空白分隔，因為和 API 的參數格式（id of coins, comma-separated if querying more than 1 coin
）較為一致

`2022/03/17`
- 改用`gspread`套件，因為`pygsheets`年久失修，Google Sheets API 驗證一直過不了，錯誤訊息：`Client secrets must be for a web or installed app.`
- 完成取得與更新 sheet 內容測試

`2022/03/18`
- 完成主要功能
- 調整寫入 sheets 的順序與 config 一致，以免新增幣種時，原來的順序會被打亂
- 新增兩種可能錯誤訊息
- 新增可單獨更新 coins.csv 的 py 檔，可另安排週期性事件或於必要時執行
- 新增可自訂 Google sheet 名稱

`2022/03/19`
- 新增 demo 圖片
- 新增 crontab job，此部分較麻煩因為 crontab process 會使用獨立的 shell
  - 修正路徑，以免 crontab process 出現路徑錯誤
- 新增獨立 logging，不使用全域設定