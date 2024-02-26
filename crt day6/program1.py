#write a python program shopping mall 5% discount for men and 7% discount for women and individual discount for each item there purches is 3*no. items customers they purchase calculate the total bill?
'''no_of_items=input()
sp1,dm=map(int,input().split())
sp2,dw=map(int,input().split())
total_bill=sp1*(dm/100)
total_bill=sp2*(dw/100)
individual_items=3*no_of_items
print(sp1-total_bill)
print(sp2-total_bill)
print(individual_items)'''

#discount
d={}
n=int(input("enter no.of prizes"))
for i in range(n):
    k=input("enter items:")
    v=int(input("enter item prize:"))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter gender:")
if g=="male":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items - prices : discount-prices")
for i in d:
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"Total bill:{bill}")
    
