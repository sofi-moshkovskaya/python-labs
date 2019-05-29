#Даний файл дійсних чисел, що містить елементи прямокутної матриці (за рядками), 
#   причому перший елемент файлу містить кількість стовпців матриці. 
#   Створити новий файл тієї ж структури, що містить матрицю, транспоновану до вихідної.


try:
    
    with open("matrix.txt",'r') as orig:
        columns=int(orig.read(1))

        #читаем из файла строку цифр и разбиваем ее на список элементов матрицы
        matrix=str(orig.read()).split()
       
        with open("transp_matrix.txt", 'w') as copy:
            copy.write(str(columns))

            #записываем в файл только элементы i-того столбца, транспонируя матрицу
            for i in range (0,5):
                #print(matrix[i::columns])
                copy.writelines("%s " % s for s in matrix[i::columns])
            print("Транспонированная матрица успешно создана!")

except IOError:
    print("No file has been found.")

