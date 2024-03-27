import json

#增加一個特定商品數量
def lunch(item):

    with open("./cogs/mod/storage.json" ,"r",encoding = "utf-8") as file:
        storage = json.load(file)
    for i in range(0,9):
        if storage["storage"][i]["ename"] == str(item):
            storage["storage"][i]["amount"]+=1
            break
    with open("./cogs/mod/storage.json" ,"w",encoding = "utf-8") as file:
        json.dump(storage,file,indent=2)

#刪除一個特定商品數量
def delete(item):

    with open("./cogs/mod/storage.json" ,"r",encoding = "utf-8") as file:
        storage = json.load(file)
    for i in range(0,9):
        if storage["storage"][i]["ename"] == str(item):
            if storage["storage"][i]["amount"]>0:
                num = storage["storage"][i]["amount"]
                storage["storage"][i]["amount"]-=1
            elif storage["storage"][i]["amount"]==0:
                num = 0
            break
    with open("./cogs/mod/storage.json" ,"w",encoding = "utf-8") as file:
        json.dump(storage,file,indent=2)
    return num

#歸零
def init():

    with open("./cogs/mod/zero.json" ,"r",encoding = "utf-8") as file:
        storage = json.load(file)
    with open("./cogs/mod/storage.json" ,"w",encoding = "utf-8") as file:
        json.dump(storage,file,indent=2)
    
#取得總價錢
def total():
    
    with open("./cogs/mod/storage.json" ,"r",encoding = "utf-8") as file:
        storage = json.load(file)
        sum = 0
        for i in range(0,9):
            sum += storage["storage"][i]["amount"]*storage["storage"][i]["price"]
    return sum

#取得特定商品數量
def amount(item):

    with open("./cogs/mod/storage.json" ,"r",encoding = "utf-8") as file:
        storage = json.load(file)
        for i in range(0,9):
            if storage["storage"][i]["ename"] == str(item):
                num = storage["storage"][i]["amount"]
                break
    return num

#特定商品金額
def price_i(item):

    with open("./cogs/mod/storage.json","r",encoding = "utf-8") as file:
        storage = json.load(file)
        for i in range(0,9):
            if storage["storage"][i]["ename"] == str(item):
                sym = int(storage["storage"][i]["price"])*int(storage["storage"][i]["amount"])
                break
    return sym

#將中文商品名轉為代表字串
def ename(item):

    with open("./cogs/mod/trans.json" ,"r",encoding = "utf-8") as file:
        menu = json.load(file)
        for i in range(0,9):
            if menu["storage"][i]["cname"] == str(item):
                ename = menu["storage"][i]["ename"]
                break
    return ename