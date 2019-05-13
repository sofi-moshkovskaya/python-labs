#7. Скласти опис класу для визначення одновимірних масивів рядків фіксованої довжини. 
#   Передбачити контроль виходу за межі масиву, можливість звернення до окремих рядків масиву за індексами, 
#   виконання операцій поелементного зчеплення двох масивів з утворенням нового масиву, 
#   злиття двох масивів з виключенням повторюваних елементів, а також вивід на екран елемента масиву по заданому індексу і всього масиву.


lenght=15
class Array:
 
    def __init__(self,list=[]):
        i=1;
        self.arr=list
        if len(list)==0:
            print("Введите элемент массива")
            while i!=0:
                str=input()
                self.arr.append(str[:lenght])
                i=int(input("Хотите добавить элемент?  (1-да, 0-нет)"))


    def __add__(self, other):
        res=[]; copy1=self.arr[:]; copy2=other.arr[:]
        m=len(self); n=len(other)                   #если длинна массивов разная
        if m<n:
            for b in range(0,n-m): copy1.append(str(""))
        if m>n:
            for с in range(0,m-n): copy2.append(str(""))

        for a in range(0,len(self)):
            line=(copy1[a]+' '+copy2[a]).strip()
            res.append(line)
        r=Array(res)
        return r


    def __len__(self):                  #нахождение длинны массива
        return len(self.arr)


#    def print(self):                    #вывод каждого элемента массива
#        for element in self.arr:
#            print(element)

    def __str__(self):
        return str(self.arr)


    def __getitem__(self,i):            #прямой доступ к элементу
        try:
            return self.arr[i]        #вводится 3, вывод 4 элемент
        except IndexError: print("Выход за пределы массива.")



see=['one', 'two']
test=Array(see)
test1=Array()
#test2=Array()
test3=test+test1+test1
print(test3)
