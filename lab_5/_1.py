#Даний рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за алфавітом, в стовпчик.
#20.04.2019

str=input("Введите строку:  ")
words=str.split()
words.sort()

for i in words:
    print(i)