n=int(input())
s=input()
mn=0
sm=0
for i in range(n):
  sm+=1 if s[i]=="(" else -1
  mn=min(mn,sm)
mn*=-1
print("("*mn+s+")"*(sm+mn))
