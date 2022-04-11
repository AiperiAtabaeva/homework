dev=input("язык 'python','java','javascript':")
age=int(input('возраст:'))
exp=int(input('опыт работы:'))
sal=int(input('желаемая зарплата'))
if dev in ['python','java','javascript'] and 18<=age<=65 and exp>=3 and sal<=60000:
    print('congratulation')
else:
    print('sorry')
