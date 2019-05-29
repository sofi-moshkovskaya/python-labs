#Дано ім'я файлу і ціле число N (> 1). Створити файл цілих чисел з такою назвою і записати в нього N перших позитивних парних чисел (2, 4, ...).

name="file_2.txt"
N=100

with open(name, 'w') as f:
    numbers=[i for i in range(2, N+1, 2)]
    f.writelines("%s " % i for i in numbers)



numbs=[2,4,6,8,10,12,14,16,18,20]
a=numbs[::-1]
print(a)