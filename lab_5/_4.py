#Дано два упорядкованих за спаданням списки. Об'єднайте їх в новий упорядкований за спаданням список.


list1=['hello','python','java']
list2=['kherson','ksu']

list1.sort(reverse=True)
list2.sort(reverse=True)

print(list1,'\n',list2)

newlist=list1+list2
newlist.sort(reverse=True)
print(newlist)