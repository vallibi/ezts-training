#write a python program to print prime numbers in a range using functions
def prime(n,m):
    for i in range(n,m+1):
        count=0
        for j in range(1,n+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)
n,m=int(input()),int(input())
prime(n,m)
