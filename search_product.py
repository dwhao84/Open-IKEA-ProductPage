import  webbrowser
# Example for using art_num as list, for searching product's article numbers.
art_num = ["30362919", "60362913", "80362912"]

# Open web browser fast by using For-Loop function.
for i in art_num:
    url = f"https://www.ikea.com.tw/zh/search?q= { i }"
    webbrowser.open(url)
    print(i)
