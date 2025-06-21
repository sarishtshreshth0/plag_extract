#https://atcoder.jp/contests/abc070/tasks/abc070_b

a,b,c,d=map(int,input().split())

s1=set()
s2=set()

for i in range(a,b+1):
    s1.add(i)

for i in range(c,d+1):
    s2.add(i)

s1_s2_and=s1&s2
if len(s1_s2_and)==0:
    print(0)
else:
    print(len(s1_s2_and)-1)