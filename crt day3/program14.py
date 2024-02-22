#to print the sum of composite numbers in a given range?
'''def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    if i%2!=0:
        flag=composite(i)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)'''

#to print all composite no. in range
'''def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    flag=composite(i)
    if flag==1:
        l.append(i)
print(sum(l))
print(l)'''

#to print only even composite no. in a range
def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    if i%2==0:
        flag=composite(i)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)
