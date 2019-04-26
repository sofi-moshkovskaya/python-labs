#Даний рядок, що містить повне ім'я файлу. 
#Виділіть з цього рядка ім'я файлу без розширення.

file_adress="C:\WebServers\home\testsite\www\myfile.txt"
#file_adress=input("Введите адрес файла:   ")

#1
file_name=file_adress.split('\\')[-1]
print(file_name[:-4])

#2
n=file_adress.rfind('\\')
print(file_adress[n+1:-4])