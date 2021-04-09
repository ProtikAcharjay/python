def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("give a number to get finacci: "))
print(fibonacci(num))