region=input("район 'Чон арык','Байтик','Орто сай':")
price=int(input('стоимость дома:'))
material=input("строй материала 'кирпич','пескоблок':")
size=int(input('размер участка:'))
if region in ["Чон арык","Байтик","Орто сай"]  and material in ['кирпич'] and size<=4 and price<=5000:
    print('welcome')
elif region in ["Чон арык","Байтик","Орто сай"] and material in['пескоблок'] and size<=5 and price<=40000:
    print('welcome peskoblok')
else:
    print('нет вариантов') 
