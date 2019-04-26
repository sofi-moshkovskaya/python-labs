 #У списку чисел перевірити, чи всі елементи є унікальними, тобто кожне число зустрічається тільки один раз.


print("Введите числа через пробел")
numbers=input()
numbers=numbers.split(' ')

#print(numbers)

#1
for i in numbers:
    if numbers.count(i)!=1:
        print("\nСписок содержит не уникальные элементы!")
        break
    print("\nВсе элементы списка уникальны!")


#2
numb_set=set(numbers)
if len(numbers)==len(numb_set):
    print("\nВсе элементы списка уникальны!")
else:
    print("\nСписок содержит не уникальные элементы!")
    