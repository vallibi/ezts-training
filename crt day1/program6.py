#a,b=map(int,input().split(" "))-we can write input values side by side 
'''a,b=map(int,input().split(" "))
print(a,b)'''
                                          #b=balance amount,a=withdraw amount
'''a,b=map(float,input().split(" "))
if b>a:
    if a%5==0:
        print(b-a)
    else:
        print(b)
else:
    print(b)'''


a,b=map(float,input().split(" "))
if b>a and a%5==0:
    print(b-a)
else:
    print(b)






