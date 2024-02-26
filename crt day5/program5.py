'''l,d=map(int,input().split())
lst=list(map(int,input().split()))
for i in lst:
    for j in lst:
         if i-j==d:
             flag=1
if flag==1:
    print(True)             #input=5 60 , 1 20 40 100 80 #output=true
else:
    print(False)'''
    
        
        
l,d=map(int,input().split())
lst=list(map(int,input().split()))
for i in lst:
    for j in lst:
         if i-j==d:
             flag=1
if flag==0:
    print(True)             #input=5 60 , 1 20 40 100 80 #output=false
else:
    print(False)
    
 
