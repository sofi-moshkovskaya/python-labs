#12. Створити клас для зберігання комплексних чисел. Реалізувати операції над комплексними числами: додавання, віднімання,
# множення, ділення, зведення в ступінь, добування кореня. Передбачити можливість зміни форми запису комплексного числа: алгебраїчна форма,
# тригонометрическая форма, експоненціальна форма.
import math

class Cmplx:
    def __init__(self, re, im):
        self.re = re
        self.im = im
        self.mod=(re**2+im**2)**0.5

    def __add__(self, obj):
        res=Cmplx(self.re + obj.re,self.im + obj.im)
        return res
    
    def __sub__(self, obj):
        res=Cmplx(self.re - obj.re,self.im - obj.im)
        return res

    def __mul__(self, obj):
        res=Cmplx(self.re * obj.re - self.im * obj.im, self.im * obj.re + self.re * obj.im)
        return res

    def __truediv__(self, obj):
        re=(self.re*obj.re+self.im*obj.im)/(obj.re**2+obj.im**2)
        im=(obj.re*self.im-self.re*obj.im)/(obj.re**2+obj.im**2)
        res=Cmplx(re,im)
        return res

    def __str__(self):
      return '({re:.2f} + {im:.2f}i)'.format(re=self.re, im=self.im)
    
    def to_trig(self):
       self.arg=math.degrees(math.atan(self.im/self.re))        #phi
       self.cos=math.degrees(math.cos(self.arg))
       self.sin=math.degrees(math.sin(self.arg))
       return '{r:.2f}(cos{phi:.2f} + sin{phi:.2f}i)'.format(r=self.mod, phi=self.arg)
    
    def __pow__(self, other):
        self.arg=math.degrees(math.atan(self.im/self.re))
        self.cos=math.degrees(math.cos(self.arg))
        self.sin=math.degrees(math.sin(self.arg))
        return '{r:.2f}(cos{phi:.2f} + isin{phi:.2f})'.format(r=self.mod**other, phi=self.arg*other)
        #return (self.mod**other)*(math.cos(self.arg*other)+'i'+math.sin(self.arg*other)
    
    def to_exp(self):
        return '{r:.2f} e^{phi:.2f}i'.format(r=self.mod, phi=self.arg)

    def root(self, numb):
        roots=[]
        for n in range(0,numb):
            r=self.mod**(1/numb)
            cos=math.cos((self.arg+2*n*math.pi)/numb)
            sin=math.sin((self.arg+2*n*math.pi)/numb)
            res=Cmplx(r*cos,r*sin)
            roots.append(str(res))
        return roots
 

a = Cmplx(8, 0)
b = Cmplx(1,3)

print("a = ",a)
print("b = ",b)
print("a + b = ",a+b)
print("a - b = ",a-b)
print("a * b = ",a*b)
print("a **7 = ",a**7)
print("a/b = ",a/b)
print("Тригонометрическая форма b:   ",b.to_trig())
print("Експоненциальная форма b:     ",b.to_exp())
print("Корень 3 степени из а:   ",a.root(3))
