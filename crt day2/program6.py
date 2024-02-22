#write a python program to print reverse of a num
n=int(input())
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit                 #example
    n//=10
print(rev)                          #168/10=8remainder,so digit=rev=8,168//10=16
                                    #16/10=6remainder,so digit=6,rev=8*10+6=86, 16//10=6
                                    #1/10=1remainder,so digit=1,rev=86*10+1=861, 1//10=0


