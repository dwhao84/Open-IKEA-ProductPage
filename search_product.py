import  webbrowser
art_num = ["30362919", "60362913", "80362912"]

for i in art_num:
    url = f"https://www.ikea.com.tw/zh/search?q= { i }"
    webbrowser.open(url)
    print(i)
