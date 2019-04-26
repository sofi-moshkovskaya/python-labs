#У програмі задані місяць і рік двох дат. Користувач вводить ще одну дату (тільки місяць і рік).
# Визначити, чи належить третя дата діапазону від першої дати до другої включно. 
# Завдання вирішити з використанням структури даних.

from datetime import date

date1=input("Введите начальную датy диапазона (месяц и год):    ")
date1=date1.split(' ')      #вернет кортеж
m1,y1=date1                 #разбитие кортежа

date2=input("Введите нконечную датy диапазона (месяц и год):    ")
date2=date2.split(' ')      #вернет кортеж
m2,y2=date2                 #разбитие кортежа

date3=input("Введите дату для проверки (месяц и год):    ")
date3=date3.split(' ')
m3,y3=date3

#создание даты
date_start=date(int(y1),int(m1),1)
date_end=date(int(y2),int(m2),1)
date_check=date(int(y3),int(m3),1)

#print("start date: ", date_start,"\nend date:", date_end)

print("\n\n\nДата в диапазоне:\n",date_start<=date_check<=date_end)
