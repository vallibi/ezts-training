#write a python program to remove consecutive to duplicates in string
s1=input()
s2=s1[0]
for i in range(1,len(s1)):
    if s1[i-1]!=s1[i]:
        s2+=s1[i]
print(s2)
