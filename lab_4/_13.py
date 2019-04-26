#13. Дано натуральне число n> 1. Виведіть всі прості множники цього числа в порядку зростання з урахуванням кратності.



def task(n):
    print(1)
    for i in range(2,n+1):
        while(isPrime(i) and n%i==0):
            n/=i
            print(i)
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input("Введите число: "))

task(n)