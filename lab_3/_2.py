#2. По залишку від ділення цілої частини значення функції y = log (x² + ab) на 7 вивести день тижня. Значення змінних а, b, x 
#   отримати випадковим чином на зазначеному користувачем інтервалі.
import random
import math 

print("Введите интервал для чисел а, b, x")
start=int(input())
end=int(input())

a=random.randint(start, end)
b=random.randint(start, end)
x=random.randint(start, end)
str=''

print(a,b,x)

def week_day(a,b,x):
    y=int(math.log10(x**2+a*b))     #сразу находим целую часть значения функции
    day=y%7
    if day==0:
        str='monday'
    elif day==1:
        str='tuesday'
    elif day==2:
        str='wednesday'
    elif day==3:
        str='thursday'
    elif day==4:
        str='friday'
    elif day==5:
        str='saturday'
    else: 
        str='sunday'
    return str

str=week_day(a,b,x)
print("День недели - ", str)

