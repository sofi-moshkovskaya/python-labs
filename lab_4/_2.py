#2. Дано перший член і знаменник геометричної прогресії. Написати рекурсивну функцію знаходження n-го члена прогресії
#   і знаходження суми n перших членів прогресії


def geometricProgression(b, q, n):
    if n == 1:
        return b
    return geometricProgression(b, q, n - 1) * q

def geometricSum(b, q, n):
    if n == 1:
        return b
    #return b * q ** (n - 1) + geometricSum(b, q, n - 1)
    return geometricProgression(b,q,n)+ geometricSum(b,q,n-1)

b = int(input("Введите число: "))               
q = int(input("Введите знаменатель: "))         
n = int(input("Введите N: "))                   

print("--------------------------------")
print("Прогрессия:", geometricProgression(b, q, n))
print("Сумма N-первых членов:", geometricSum(b, q, n))