Q,H,S,D = map(int, input().split())
N = int(input())

q = Q * 8
h = H * 4
s = S * 2
d = D

rlt = 0

lst1 = [Q, H, S, D]
lst2 = [q, h, s, d]
lst3 = [q, h, s]

while N > 0:
  if N >= 2:
    a = lst2.index(min(lst2))
  else:
    a = lst3.index(min(lst3))
  if a == 0:
    rlt += lst1[0] * N * 4
    N = 0
  elif a == 1:
    rlt += lst1[1] * N * 2
    N = 0
  elif a == 2:
    rlt += lst1[2] *N
    N = 0
  else:
    rlt += lst1[3] * (N // 2)
    N = N % 2

print(rlt)
