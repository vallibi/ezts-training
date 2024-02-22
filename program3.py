#to print the product of the elements in the matrix
'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))   
print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)

#output
rows:3
coloums:3
1 2 3
4 5 6
7 8 9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
362880'''



r,c=int(input("rows:")),int(input("coloums:"))
l=[0]*r
for i in range(r):
    l[i]=(list(map(int,input().split())))   
print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)


#output
rows:3
coloums:3
1 2 3
4 5 6
7 8 9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
362880




