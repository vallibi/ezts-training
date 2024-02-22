#to print sum of coloumns in a matrix?
'''r,c=int(input("rows:")),int(input("coloumns:"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
        sum+=i[c-1]
print(sum)'''


'''r,c=int(input("rows:")),int(input("coloumns:"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
        sum+=i[c-2]
print(sum)'''


r,c=int(input("rows:")),int(input("coloumns:"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
        sum+=i[c-3]
print(sum)




