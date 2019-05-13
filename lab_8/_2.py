#2. Створіть клас з ім'ям train, що містить поля: назва пункту призначення, номер поїзда, час відправлення.
#   Ввести дані в масив з п'яти елементів типу train, впорядкувати елементи за номерами поїздів. 
#   Додати можливість виведення інформації про потяг, номер якого введено користувачем. 
#   Додати можливість сортування масив по пункту призначення, причому поїзда з однаковими пунктами призначення 
#   повинні бути впорядковані за часом відправлення.

#   Moshkovskaya Sophia
from datetime import time

class Train:
    def __init__(self, dest, numb, time):
        self.destination=dest
        self.number=numb
        self.dep_time=time

    def __info__(self):
        print("Пункт назначения:    ",self.destination)
        print("Номер поезда:        ", self.number)
        print("Время отправки:      ",self.dep_time,'\n')

def __dest_sort__(list):
    list.sort(key=lambda Train: Train.dep_time)
    list.sort(key=lambda Train: Train.destination)


t1=Train("Киев", 322, time(22,10))
t2=Train("Николаев", 144, time(8,3))
t3=Train("Киев",782, time(13,15))
t4=Train("Харьков", 521, time(7,38))
t5=Train("Житомир",386, time(13))


station=[t1,t2,t3,t4,t5]


i=1
while i!=5:
    print("Выберите действие:\nСортировка по пункту назначения - 1\nПоказать информацию о поезде - 2\nПоказать список поездов - 3\nСортировка по номеру поезда - 4\nВыход - 5")
    i=int(input())
    if i==1:
        __dest_sort__(station)
    elif i==2:
        n=int(input("Введите номер поезда:  "))
        n-=1
        station[n].__info__()
    elif i==3:
        for i in station:
            i.__info__()
    elif i==4:
        station.sort(key=lambda Train: Train.number)
