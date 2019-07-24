a=int(input())
d=list(map(int,input().split()))
c=0
for i in range(len(d)):
    f=d[0]
    d.pop(0)
    if f in d:
        d.append(f)
        c+=1
    else:
        c='unigue'
print(c)
