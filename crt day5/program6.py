s=input()
for i in s:
    if s.count(i)>i:
        print(i)
        break
else:
    print('.')
