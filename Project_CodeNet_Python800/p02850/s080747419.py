import sys
input = sys.stdin.readline
def main():
  from collections import deque
  from collections import defaultdict
  n=int(input())
  ab=[list(map(int,input().split())) for _ in range(n-1)]
  g=[[] for _ in range(n)]
  for i,abi in enumerate(ab):
    a,b=abi
    g[b-1].append(a-1)
    g[a-1].append(b-1)
  todo=deque([(0,-1)])
  dc={}
  while len(todo)>0:
    a,pc=todo.popleft()
    l=g[a]
    c=0
    for li in l:
      d,e=min(a,li),max(a,li)
      if (d,e) not in dc:
        c+=1 if c+1!=pc else 2
        dc[(d,e)]=c
        todo.append([li,c])
  print(max(dc.values()))
  for a,b in ab:
    print(dc[(a-1,b-1)])
if __name__=='__main__':
  main()
