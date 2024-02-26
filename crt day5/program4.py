#write a python program to check whether the given string is anagram or not - it consits same elements
'''s1,s2=map(str,input().split())
if len(s1)==len(s2):
    if sorted(list(s1)) == sorted(list(s2)):
        print(True)
    else:
        print(False)
else:
    print(False)'''


'''s1,s2=map(str,input().split())
print(sorted(list(s1)))
print(sorted(list(s2)))
if len(s1) == len(s2):
    if sorted(list(s1)) == sorted(list(s2)):
        print(True)
    else:
        print(False)
else:
    print(False)'''

#anagram using dictionary
d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=llist(d.values())
if len(l[0]) == len(l[1]):
    if sorted(list(l[0])) == sorted(list(l[1])):
        print(True)
    else:
        print(False)
else:
    print(False)
