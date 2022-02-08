a,m,d,n=map(int,input().split())
cnt=1
while cnt<n:
  a=a*m+d
  cnt+=1
print(a)
