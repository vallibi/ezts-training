#write a python program to check whether it is a strong no. or not using functions?
#strong number=145=1!+4!+5!-sum of the factorializations of individual nummbers
def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        print("strong")
    else:
        print("not strong")
n=int(input())
strong(n)
            
            

         
            
    
