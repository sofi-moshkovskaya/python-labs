#3. Створити клас з двома змінними. Додати функцію виведення на екран і функцію зміни цих змінних. Додати функцію, яка знаходить суму значень цих змінних, 
#   і функцію яка знаходить найбільше значення з цих двох змінних.


class Example:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print("Значение х:  ",self.x)
        print("Значение у:  ",self.y)

    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y[0]=y

    def sum(self):
        return self.x+self.y

    def max(self):
        return max(self.x, self.y)


a=Example(3,7.5)
a.show()
print(a.sum())
print(a.max())

a.set_x(10)
print(a.max())