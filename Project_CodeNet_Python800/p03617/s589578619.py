q,h,s,d = map(int,input().split())
n = int(input())
cheep = min((q*4),(h*2),s)
if cheep * 2 <= d:
  print(cheep*n)
else:
  n1 = n % 2
  print(n // 2 * d + n1 * cheep)
