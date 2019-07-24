a=int(input())
d=list(map(int,input().split()))
for i in range(len(d)):
    f=d[0]
    d.pop(0)
    if f in d:
        d.append(f)
    else:
        print(f)
