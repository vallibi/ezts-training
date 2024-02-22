#strong no. using strings and recursion
'''def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=factorial(int(i))
    if sum == x:
        return "strong number"
    else:
        return "not a strong number"
x=int(input())                         #input=145,output=strong no.
print(strong(x))'''

#in a range

def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=factorial(int(i))
    if sum == x:
        print(x)
a,b=int(input()),int(input())
for i in range (a,b+1):                            #input=100 100000,output=145 40..
    strong(i)







