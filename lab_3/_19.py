#   19. Описати функцію IsSquare (K) логічного типу, яка повертає True, якщо цілий параметр K (> 0) 
#   є квадратом деякого цілого числа, і False в іншому випадку. З її допомогою знайти кількість квадратів в наборі з 10 цілих позитивних чисел.
import math

def IsSquare(k):
    real=math.sqrt(k)
    return real.is_integer()


spisok=[]
print("Введите 10 натуральных чисел через ENTER")

for i in range (0,10):
    spisok.append(int(input()))

print("\nИз этих чисел квадратом некого числа есть:")
for i in range(0,10):
    result=IsSquare(spisok[i])
    if result:
        print(spisok[i])