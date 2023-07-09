import easyocr
from datetime import date
import torch
from openpyxl import workbook,load_workbook

device = torch.device("mps")

reader = easyocr.Reader(['ch_sim',"en"],gpu=True)

folder_path = '/Users/hanshan/Desktop/稀土'

# List of all your jpeg files
file_list = ['6.12.png', '6.13.png', '6.14.png', '6.15.png',"6.16.png","6.19.png","6.20.png","6.21.png",
             "6.26.png","6.27.png","6.28.png","6.29.png"] # replace with your actual files

wb=load_workbook("/Users/hanshan/Desktop/稀土/稀土综合价格分析.xlsx")

ws=wb["chart_data"]

# ws=wb["chart_data"]

for file in file_list:
    result = reader.readtext(file, detail=0)
    today=date.today()
    index日期=today.strftime("%Y.%m.%d")

    # We can put all these in a list to reduce the amount of code.
    item_names = ["氧化镨钕", "镨钕金属", "氧化镝", "镝铁合金", "氧化铽", "金属铽", 
                  "金属镧", "金属铈", "金属镨", "金属钕", "钆铁合金", "钬铁合金", 
                  "金属钴", "金属镓", "电解铜", "电解铝", "海绵锆", "铌铁合金", 
                  "硼铁合金", "原料纯铁"]

    item_prices = []
    for item in item_names:
        try:
            index = [i for i, x in enumerate(result) if x == item][0] + 3
            item_prices.append(result[index])
        except IndexError:  # item not in result
            item_prices.append("")  # Insert empty string if item was not found.

    ws.append([index日期] + item_prices)
    
wb.save("/Users/hanshan/Desktop/稀土/稀土综合价格分析.xlsx")
