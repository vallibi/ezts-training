#to print the sum of odd no. in a range?
n,m=int(input()),int(input())
l=[i for i in range(n,m+1) if i%2!=0]
print(sum(l))
