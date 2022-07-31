import math
import requests
import polygon
import numpy as np
import regex as re

#find USD RUB fx rate
reponse = requests.get(
    'https://api.polygon.io/v2/aggs/ticker/C:USDRUB/prev?adjusted=false&apiKey=5b87jQkveaTEkI0jaSDwn_x5HpcOGzeB')
string = str(reponse.text)
step=string.find('"c":')#return index of first literal only, which is "

print("USD/RUB rate: "+string[step+4]+string[step+5]) # str !
USDRUB=string[step+4]+string[step+5]    # str needs to be converted to float

#Find gold price
reponse1 = requests.get(
    'https://api.polygon.io/v2/aggs/ticker/C:XAUUSD/prev?adjusted=false&apiKey=5b87jQkveaTEkI0jaSDwn_x5HpcOGzeB')
string1 = str(reponse1.text)
step1=string1.find('"c":')
gold_price =string1[step1+4]+string1[step1+5]+string1[step1+6]+string1[step1+7]+string1[step1+8]+string1[step1+9]+string1[step1+10]
def converter(today_usdrub):
    price = 5000 / today_usdrub * 28.35  # 到六月底
    print("The Gold Price should be: $" + str(round(price, 2)) + "/oz")  # 小数点后两位



converter(float(USDRUB))    #conver str to num
print("Price of XAUUSD is : $"+gold_price+"/oz")
difference = round(float(gold_price)/ (5000 / float(USDRUB) * 28.35),2) # gold price is str need to be convert to num
print("It is trading at " +str(100*difference)+"% of the RCB floor price.")
print("Stop use it at end of June!")