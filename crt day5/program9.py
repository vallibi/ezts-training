#to print average of each student marks given in student data base in nested dictionary ?
n=int(input("enter the no of students:"))
m=int(input("enter the no of subjects:"))
d={}
for i in range(n):
    k=input("enter rollno:")
    v={}
    for j in range(m):
        sub=input("enter subject name:")
        marks=int(input("enter marks:"))
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i} : {sum(1)/m}")
