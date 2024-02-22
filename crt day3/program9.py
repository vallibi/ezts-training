#to print factorial of given number?
def factorial(n):
    if n < 1 :
        return 1
    else:
        return n*factorial(n-1)
n=int(input())                         #input=5,output=120
print(factorial(n))

