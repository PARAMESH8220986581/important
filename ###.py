
n = int(input())
L = list(map(int,input().split()))
s=0
for i in range(s,len(L)):
  if L[i] in L:
    if (L.count(L[i]))>=2:
      s+=1
      print(s)
    if s>=2:
      print(L[i])
      
