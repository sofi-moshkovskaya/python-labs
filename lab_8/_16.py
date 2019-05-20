#16. Створити абстрактний клас Figure з методами обчислення площі та периметра, а також методом, що виводить інформацію про фігуру на екран.
# Створити похідні класи: Rectangle (прямокутник), Circle (коло), Triangle (трикутник) зі своїми методами обчислення площі і періметра.
# Создать масив n фігур і вивести повну інформацію про фігури на екран.


import math

class Figure:
    def __init__(self):
        pass

    def square(self):
        pass

    def perimeter(self):
        pass

   
class Rectangle(Figure):

    def __init__(self, x, y):
        self.lenght=x
        self.width=y

    def square(self):
        return self.lenght*self.width
    
    def perimeter(self):
        return 2*(self.lenght+self.width)

    def __str__(self):
        return '\nПрямоугольник\nДлина:    {0}\nШирина:    {1}\nПериметр:    {2}\nПлощадь:    {3:.3f}'.format(self.lenght, self.width, self.perimeter(), self.square())


class Circle(Figure):

    def __init__(self,r):
        self.radius=r

    def square(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2*self.radius*math.pi

    def __str__(self):
        return '\nКруг\nРадиус:   {0}\nДлина:    {1:.3f}\nПлощадь:    {2:.3f}'.format(self.radius, self.perimeter(), self.square())


class Triangle(Figure):

        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c

        def square(self):
            p=(self.a+self.b+self.c)/2
            return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

        def perimeter(self):
            return (self.a+self.b+self.c)

        def __str__(self):
            return '\nТреугольник\nСтороны треугольника:      {0}, {1}, {2}\nПериметр:     {3}\nПлощадь:    {4:.3f}'.format(self.a, self.b, self.c, self.perimeter(), self.square())



c=Rectangle(5,17)
b=Circle(36)
t=Triangle(3,2,48)
g=Rectangle(8,11)
k=Triangle(7,19,45)
m=Triangle(47,10,14)
p=Circle(28)

array=[c,b,t,g,k,m,p]
for el in array:
    print(el)