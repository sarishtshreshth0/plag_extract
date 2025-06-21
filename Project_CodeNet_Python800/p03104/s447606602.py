A,B=map(int,input().split())

def calc_xor(n): #nは0以上
  if n%2==0:
    p=n//2
    if p%2==0:
      q=0
    else:
      q=1
    return q^n
  else:
    p=(n+1)//2
    if p%2==0:
      q=0
    else:
      q=1
    return q

#print(calc_xor(A-1))
#print(calc_xor(B))
print(calc_xor(A-1)^calc_xor(B))
