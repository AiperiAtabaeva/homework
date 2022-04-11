o=int(input('оклад:'))
dk=int(input("количесво календарных дней:"))
df=int(input("фактически отработанные дни:"))
p=int(input("премии:"))
h=13
y=int(input("удержания:"))
sal=(o/dk*df+p)*((100-h)/100)-y
print(int(sal))
