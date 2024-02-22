#if chocolates are less than the childrens 
'''children,choco=int(input()),int(input())
x=children-choco
if choco < children:
    print(x/4)                             #each packet contains 4 chocolates
else:                                       #20-12=8   8/4=2
    print(0)'''



children,choco=int(input()),int(input())
x=children-choco
if choco < children:
    if x%4==0:
        print(x//4)
    else:
        print((x//4)+1)
else:
    print(0)
                                             #condition x=10-9=1
                                             #but for (x/4) we are getting a float value 0.
                                              #for (x//4) we are getting a int value 1
    
