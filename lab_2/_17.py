#17. Дано ціле число N (> 1). Знайти найменше ціле число K, при якому виконується нерівність 3K> N.
n=int(input("Input the intenger nubmer  "))
k=0
while 3*k<=n:
    k+=1
print(k)