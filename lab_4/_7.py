#7. Написати рекурсивну функцію, що визначає, чи є симетричною частина рядка S, починаючи з i-го елемента і закінчуючи j-м.
 
def isSymmetrical(str, i, j):
    # Если i равняется или больше j
    # Если половина пройдена
    if j <= i:
        return True
    # Если символы разные
    if str[i].lower() != str[j].lower():
        return False;
    # Продолжаем со смещением индексов i -> следующий (i+1), j -> предыдущий (j-1)
    return isSymmetrical(str, i + 1, j - 1)

str = input("Введите строку: ")           
i = int(input("Введите i: ")) - 1          
j = int(input("Введите j: ")) - 1       

print(isSymmetrical(str, i, j))         