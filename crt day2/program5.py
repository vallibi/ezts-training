#write a python program to ch3eck whether the given number is perfect or not
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect num")
else:
    print("not")
        
    
