#2. Дано три цілих числа. Знайти кількість додатних чисел в початковому наборі.
a=int(input("Введите первое целое:  "))
b=int(input("Введите второе целое:  "))
c=int(input("Введите третье целое:  "))
amount=0

if a>0: amount+=1
if b>0: amount+=1
if c>0: amount+=1

print("Количество положительных: ", amount)