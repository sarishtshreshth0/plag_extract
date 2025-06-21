N,h,u=map(int,input().split())
S = input()
kaigai=0
goukei=0
for i in range(0,N):
  if S[i]=='a' and goukei<h+u:
    print("Yes")
    goukei+=1
  elif S[i]=='b'and goukei<h+u and kaigai<u:
    print("Yes")
    goukei+=1
    kaigai+=1
  else:
    print("No")