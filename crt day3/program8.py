#write a python program to print sum of n natural no.using recursion
def printing(n):
    if n < 1:
        return 1              #input=10 or any value,output for 10=10 9 8 7 6 5 4 3 2 1 ,sum=56
    else:
        print(n)
        return n+printing(n-1)
n=int(input())
sum=printing(n)
print(sum)


