#write a python program to print amstrong no. in a range using function
def amstrong(n,m):    
    for i in range(n,m+1):    #100-1001
        sum=0
        x=i                   #100   x=100 ,1**3+0**3+0**3=1,sum=1   x=101,1**3+0**3+1**3=2
        while i > 0:
            temp=n%10
            sum+=temp**3
            i//=10
        if sum == x:          #1==100  so,sum is not equals to x ,now repeat the loop then x=101   
            print(x)
n,m=int(input()),int(input()) #100-1000
amstrong(n,m)

    
