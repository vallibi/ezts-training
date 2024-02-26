#write a python program to take dictionary as input and print keys and values of the dictionary which is take in a runtime?
'''n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
print(d)'''


#another method   
'''n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print("key:",i,"","value:",d[i])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)'''


#types of print statements

#by using f function in print statement:
'''n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print(f"key:{i} value:{d[i]}")
for i in d.keys():
    print(i)
for i in d.values():
    print(i)'''
#by using format:
'''n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print(f"key:{i} value:{d[i]}")
    print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)'''
#by using (,):
n=int(input("Enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print("key:",i,"","value:",d[i])
    print(f"key:{i} value:{d[i]}")
    print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)













































































































































































    

