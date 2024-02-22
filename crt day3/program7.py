#write a python program to print n natural no. using recursion?

'''def printing(n):
    if n < 1:
        return 1
    else:                       #output= 10 9 8 7 6 5 4 3 2 1
        print(n)
        printing(n-1)
n=10
printing(n)'''


'''def printing(n):
    if n < 1:
        return 1              #output= 1 2 3 4 5 6 7 8 9 10
    else:
        printing(n-1)
        print(n)
n=10
printing(n)'''




def printing(n):
    if n < 1:
        return 1              #input=50 or 20 or any value, output=1----50,1----20
    else:
        printing(n-1)
        print(n)
n=int(input())
printing(n)


