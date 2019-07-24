a=int(input())
d=list(map(int,input().split()))
for i in range(len(d)):
    f=d[i]
    d.pop(i)
    if f in d:
        d.insert(-1,f)
    else:
        print(f)
