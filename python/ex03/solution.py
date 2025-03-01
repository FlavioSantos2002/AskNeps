def fibo(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))  # Saída: 8




#5 --> 1 1+1=2 2+1=3 3+2=5 5+3=8