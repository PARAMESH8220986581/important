a=input().split()
d=set(map(int,input().split()))
s=set(map(int,input().split()))
if (s.issubset(d)):
    print('YES')
else:
    print('NO')
