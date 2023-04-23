# sum of n - numbers
def summa(n):
    if n==0:
        return 0
    else:
        return n + summa(n-1)
print(summa(0))


#  factorial
def factor(n):
    if n==0:
        return 1
    else:
        return n*factor(n-1)

print(factor(4))

# fibonachi numbers

def fib(n):
    a=[]
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))
    