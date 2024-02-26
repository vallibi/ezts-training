def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return "composite"
    else:
            return "prime"
n=int(input())              #input=10 #output={1: 'prime', 2: 'prime', 3: 'prime', 4: 'composite', 5: 'prime', 6: 'composite', 7: 'prime', 8: 'composite', 9: 'composite', 10: 'composite'}
d={}
for i in range(n):
    key=i+1
    value=isprime(i+1)
    d[key]=value
print(d)


def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return "composite"
    else:
            return "prime"
m=int(input())


