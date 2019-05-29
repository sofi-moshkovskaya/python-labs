#13. Даний рядковий файл. Створити новий строковий файл, в якому рядки з вихідного файлу розташовувалися б в 
#   лексикографічному порядку, тобто за зростанням кодів їх символів, починаючи з першого символу.

try:
    with open("до.txt",'r') as orig:
        text=orig.readlines()
        text.sort()
        with open("после.txt", 'w')as copy:
           copy.writelines("%s" % i for i in text)
        print("Отсортированная копия файла успешно создана!")
except IOError:
    print("No file has been found.")

