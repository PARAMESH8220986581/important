import sys, string, math
k,n= input().split()
k,n = int(k), int(n)
L = [ int(x) for x in input().split()]
for i in range(0,n) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum(L[a-1:b]))
