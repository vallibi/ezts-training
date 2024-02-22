#write a python program to print the count of ovels in both even and odd positions?
s1=input()
ec,oc=0,0
for i in range(len(s1)):
    if i%2==0:
        if s1[i] in "aeiouAEIOU":
           ec+=1
     else:
        if s1[i] in "aeiouAEIOU":
           oc+=1
print(ec,oc)
