#OMG
d={}
n,m=map(int,input().split())
for i in range(n):
    key,value=map(str,input().split())
    d[key]=value
for i in range(m):
    key1,value1=map(str,input().split())
    for i in d:
        if d[i] == value1[:-1]:
            print(f"{key1} {value1} #{i}")
    
    
