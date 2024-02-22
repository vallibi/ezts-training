#finding lowcost tv out of two
#a,b=cost of tv,c,d=discounts of tv
'''a,b,c,d=map(int,input().split(" "))
if (a-c)<(b-d):
    print("first")
elif (a-c)>(b-d):
    print("second")
else:
    print("any")'''

#percentage discount
a,b,c,d=map(int,input().split(" "))
fa=a-a*c//100
fb=b-b*d//100
if fa<fb:
    print("first")
elif fa>fb:
    print("second")
else:
    print("any")



