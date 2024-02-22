#pizzas

'''f,p=map(int,input().split(" "))
x=f*p
if x%4==0:
    print(x//4)
else:
    print((x//4)+1)'''


'''f,p=map(int,input().split(" "))
if ((f*p)%4)==0:
    print((f*p)//4)
else:
    print(((f*p)//4)+1)'''



'''print((f*p)//4) if ((f*p)%4)==0  else print(((f*p)//4)+1)'''





import math
f,p=map(int,input().split(" "))
x=f*p
y=math.ceil(x/4)
print(y)
