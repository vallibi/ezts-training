#write a python program to print sum of max and min element in a matrix using tuple?
'''r,c=int(input("rows:")),int(input("coloumns:"))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    print(i)


#output
rows:3
coloumns:3
1 2 3
4 5 6
7 8 9
(1, 2, 3)
(4, 5, 6)
(7, 8, 9)'''


'''r,c=int(input("rows:")),int(input("coloumns:"))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(max+min)

#output
rows:3
coloumns:3
1 2 4
5 8 10
12 14 16
(1, 2, 4)
(5, 8, 10)
(12, 14, 16)
17          #max value in matrix=16,min value in matrix=1'''



r,c=int(input("rows:")),int(input("coloumns:"))
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
print(max+min)

#output
rows:3
coloumns:3
1 2 4
5 8 10
12 14 16
((1, 2, 4), (5, 8, 10), (12, 14, 16))
(1, 2, 4)
(5, 8, 10)
(12, 14, 16)
17









