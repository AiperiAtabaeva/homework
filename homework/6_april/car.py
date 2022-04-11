car=input("модель 'lexus', 'toyota':")
age=int(input("год:"))
mile=int(input('пробег выберите 150000 или 200000:'))
col=input("цвет 'white','grey':")
rul=input("руль 'left','right':")
host=int(input('количество владедельцов:'))
price=int(input('цена в долларах:'))
if car in ['lexus', 'toyota'] and age>=2004 and mile==150000 and col in ['white','grey'] and rul in ['left'] and host<=2 and price<=10000:
    print("buy it")
elif car in ['lexus', 'toyota'] and age>=2004 and mile==200000 and col in ['white','grey'] and rul in ['left'] and host<=2 and price<=8000:
    print('ok buy it')
else:
    print('loser')
