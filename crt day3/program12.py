#write a python program to remove duplicates in a list ?
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)    #input=1 2 3 4 4 5,output=1 2 3 4 5
print(l1)

