n = int(input());
a = list(map(int,input().split()))

ans = 0;
s = [0]*(n+1);
m = {};
for i in range(0,n):
  s[i+1] = s[i]+a[i];
for i in range(0,n+1):
  m.setdefault(s[i],0);
  m[s[i]]+=1;
for v in m.values():
  ans += v*(v-1)//2
print(ans);