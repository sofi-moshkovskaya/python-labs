#12. Перевірити, чи є число досконалим
#досконалим числом називається натуральне число, що дорівнює сумі всіх своїх власних дільників
# (тобто натуральних дільників, відмінних від самого числа).


number=int(input("Введіть натуральне число:    "))

i=1;sum=0
for i in range (i,number):
    if number%i==0:
        sum+=i

if sum==number:
    print("Число досконале!")
else:
    print("Число не досконале!")