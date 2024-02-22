#to print avg of max and min element in a matrix  using tuple
'''r,c=int(input("rows:")),int(input("coloumns:"))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print((max+min)//2)'''



r,c=int(input("rows:")),int(input("coloumns:"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
        sum+=j
print(sum)
print(sum/(r*c))
