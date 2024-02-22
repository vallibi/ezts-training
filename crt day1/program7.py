#write a python program to check whether it is a leap year or not?

'''a=int(input("year:"))
if a%400==0: 
    print("it is a leap year")
elif a%4==0 and a%100!=0:
    print("it is a leap year")
else:
    print("not a leap year")'''

a=int(input("year:"))
if a%400==0 or a%4==0 and a%100!=0: 
    print("it is a leap year")
else:
    print("not a leap year")

