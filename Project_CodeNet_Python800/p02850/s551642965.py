import sys
input = sys.stdin.readline
def main():
  n=int(input())
  ab=[list(map(int,input().split())) for _ in range(n-1)]
  g=[[] for _ in range(n)]
  for i,abi in enumerate(ab):
    a,b=abi
    g[b-1].append([a-1,i])
    g[a-1].append([b-1,i])
  seen=[-1]*(n-1)
  todo=[[0,-1]]
  while len(todo)>0:
    a,ca=todo.pop()
    l=g[a]
    c=0
    for li in l:
      if seen[li[1]]==-1:
        c+=1 if c+1!=ca else 2
        seen[li[1]]=c
        todo.append([li[0],c])
  print(max(seen))
  for s in seen:
    print(s)
if __name__=='__main__':
  main()
