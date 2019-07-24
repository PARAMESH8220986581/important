
n = int(input())
L = list(map(int,input().split()))
L.sort()
s=-1
for i in range(len(L)):
  print(L[s],end="")
  s-=1
