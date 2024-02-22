#code forces
s=input()
s1="codeforces"
count=0
for i in range(len(s1)):     #coolforsez - 4   index 2,3,7 and 9 are wrong
    if s[i]!=s1[i]:
        count+=1
print(count)
