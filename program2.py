#write a python program to print sum of the given matrix?
'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))        #rows:3,coloums:3,1 2 3,4 5 6,7 8 9,[[1, 2, 3], [4, 5, 6], [7, 8, 9]], sum=45
print(l)
s=0
for i in l:
    s+=sum(i)
print(s)'''


#matrix

r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
s=0
for i in l:
    print(i)
    s+=sum(i)
print(s)

#output
#rows:3                                                 
#coloums:3
#1 2 3
#4 5 6
#7 8 9
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]
#45
