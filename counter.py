# -*- codong: utf-8 -*-

file = input('Введите путь к текстовому файлу: ')
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
counter =dict()
with open(file, "r") as f_in:
    txt = f_in.read()
    total = 0
    for item in abc:
        cnt = txt.count(item)
        if item.lower() in counter: 
            counter[item.lower()]+= cnt
        else:
            counter[item.lower()]= cnt
        total += cnt

for ltr in counter:
    print(f"{ltr} - {counter[ltr]*100/total:2.2f}%")
