A,B = map(int,input().split())
def f(B):
  return ((B+1)%2==0)*((B+1)//2%2==1) + ((B+1)%2!=0)*(((B+1)//2%2==1)^B)
print(f(A-1)^f(B))