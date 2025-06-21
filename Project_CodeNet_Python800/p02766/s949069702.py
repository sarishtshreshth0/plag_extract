# coding: utf-8
# Your code here!

n,k = map(int, input().split())
cnt = 1
a = k
while k <= n:
  k = k*a
  cnt += 1

print(cnt)