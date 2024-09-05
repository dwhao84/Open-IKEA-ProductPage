# Excel Data Processing and Web Browser Automation

這個 Python 腳本展示了如何從 Excel 文件中讀取數據，處理特定行的數據，並自動打開瀏覽器搜索 IKEA 產品的商品編號。

### 先決條件
在運行腳本之前，請確保安裝了必要package：

* Install Pandas, Openpyxl，Pandas用於處理 Excel 數據，並且 openpyxl 用於讀取 Excel 文件（.xlsx）。

```
pip install pandas openpyxl
```

* Install Webbrowser

```
import Webbrowser
```


### 腳本概述 
讀取 Excel 文件：腳本讀取 Article_Number.xlsx 的指定工作表 (Sheet1) 中的數據。
選擇行：選擇前兩行的數據並轉換為列表。
提取商品編號：從選定的行中提取商品編號，並將其展平為一個簡單的列表。
自動網頁搜尋：每個商品編號都將自動在 IKEA 台灣網站中打開搜尋頁面（https://www.ikea.com.tw/zh/search?q=...）。

### 程式碼說明

```
import pandas as pd
import webbrowser

# 讀取 Excel 文件，並選擇工作表
excel_file_name = 'Article_Number.xlsx'
df = pd.read_excel(excel_file_name, sheet_name='Sheet1')  # 指定要讀取的工作表

# 選擇前兩行數據
row_range = range(0, 3)
row_data = df.iloc[row_range].values.tolist()

# 將選中的行數據展平成單一的商品編號列表
art_num = [item for sublist in row_data for item in (sublist if isinstance(sublist, list) else [sublist])]

# 遍歷商品編號列表，並在瀏覽器中打開相應的搜尋頁面
for i in art_num:
    url = f"https://www.ikea.com.tw/zh/search?q= { i }"
    webbrowser.open(url)
    print(i)
```

## 運作方式

- 使用 `pandas` 庫來讀取 Excel 文件並處理數據。
- 使用 `.iloc` 來選擇 DataFrame 中的特定行。
- 使用 `webbrowser` 模組自動打開瀏覽器，並對每個商品編號進行搜尋。

## 使用方法

1. 將你的 Excel 文件 `Article_Number.xlsx` 放置在腳本所在目錄中。
2. 確保 Excel 文件包含名為 `Sheet1` 的工作表，並且前兩行包含要搜索的商品編號。
3. 執行腳本，腳本會為選定行中的每個商品編號自動打開瀏覽器進行搜索。

## 範例輸出

假設 Excel 文件中包含以下商品編號：

| 商品編號       |
|----------------|
| 123456         |
| 654321         |

腳本將在瀏覽器中打開以下 URL：

- [https://www.ikea.com.tw/zh/search?q=123456](https://www.ikea.com.tw/zh/search?q=123456)
- [https://www.ikea.com.tw/zh/search?q=654321](https://www.ikea.com.tw/zh/search?q=654321)

## Happy coding!
