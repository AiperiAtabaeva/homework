
print('компьютер')
memory=int(input('оперативная память:'))
size_a=int(input('размер ssd:'))
size_b=int(input('размер hdd:'))
price=int(input('цена:'))
status=input('состояние:')
if 4<=memory<=8 and size_a>=256 and price<=1000 and status=='new':
    print('компьютер подходит')
elif 4<=memory<=8 and size_b>=1000000000000 and price<=1000 and status=='new':
    print('компьютер подходит1')
else:
    print('не подходит')
