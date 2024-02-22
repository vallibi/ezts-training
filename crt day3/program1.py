#write a python program to print a smallest ovel repeating odd no. of times in the given string?
'''str1=input()
str2=""
for i in str1:
    if i in "aeiouAEIOU":                  #vallibi=a i i - ovels are coming out from given input
        print(i)'''


#to print odd vowels
'''s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":
        if s.count(i)%2!=0:              #vallibi=a(a repeats odd no. of times),i (repeats even no. of times)
            s1+=i
print(s1)'''

#minimum no. of odd vowels
s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":               #aaiiiieeeoouuuu = e   (min no.in given input which is repeating odd no. of times only) 
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))
