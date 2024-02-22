#write a python program whether the string is panagram or not (panagram=it contains all alphabets means A to z of alphabets )
import string
s=input()
s=s.lower()
s1=string.ascii_lowercase
if set(s)==set(s1):
    print("panagram")
else:
    print("not a panagram")
