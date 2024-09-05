import pandas as pd
import webbrowser

# 讀取 Excel 文件
excel_file_name = 'Article_Number.xlsx'
df = pd.read_excel(excel_file_name, sheet_name='Sheet1')  # 讀取指定的工作表

# 選擇前兩行的數據，pandas 的 iloc 支援行範圍
row_range = range(0, 3)  # 選擇前兩行
row_data = df.iloc[row_range].values.tolist()  # 使用 iloc 來選擇行，並轉換為 list
print(row_data)

art_num = [item for sublist in row_data for item in (sublist if isinstance(sublist, list) else [sublist])]

# Example for using art_num as list, for searching product's article numbers.
# Open web browser fast by using For-Loop function.
for i in art_num:
    url = f"https://www.ikea.com.tw/zh/search?q= { i }"
    webbrowser.open(url)
    print(i)
