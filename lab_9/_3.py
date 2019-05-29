#Даний файл цілих чисел. Створити новий файл, який містить ті ж елементи, що і вихідний файл, але в зворотному порядку.

try:
    with open("3.txt",'r') as orig:
        numbs=orig.read().split()
        n=numbs[::-1]
        
        with open("3_reverse.txt", 'w') as copy:
            copy.writelines("%s " %i for i in n)
            print("Копия файла успешно создана!")
except IOError:
    print("No file has been found.")
