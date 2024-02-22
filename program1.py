#write a pythion program to print the sum of even palindrome in a range and also print list of palindromes?
def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=int(input()),int(input())                  #input= 1 100 , output= [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99],sum of even no.= 240
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)
    if flag==1:
        l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l1)
print(sum(l2))

        
    
