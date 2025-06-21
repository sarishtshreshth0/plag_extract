n=int(input())
s=input()
now=0
rec=0
for i in s:
    now+=(-1)**(i==")")
    rec=min(now,rec)
f,t="",""
if rec<0:
    f="("*-rec
    now-=rec
if now>0:
    t=")"*now
print(f+s+t)