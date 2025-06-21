def makeRelation():
  visited=[False]*(N+1)
  g=0 # group
  for n in range(1,N+1):
    if visited[n]:
      continue
    q={n}
    D.append(set())
    while q:
      j=q.pop()
      for i in F[j]: # search for friend
        if not visited[i]:
          visited[i]=True
          q.add(i)
          D[g]|={i}
    g+=1
    
def main():
  makeRelation()
  #print(D)
  for g in D:
    for d in g:
      ans[d]=len(g) - len(F[d]) - len(g&B[d]) - 1
  print(*ans[1:])


if __name__=='__main__':
  N, M, K = map(int, input().split())
  F=[set() for n in range(N+1)]
  AB=[list(map(int, input().split())) for m in range(M)]
  for a,b in AB:
    F[a].add(b)
    F[b].add(a)
  B=[set() for n in range(N+1)]
  CD=[list(map(int, input().split())) for k in range(K)]
  for c,d in CD:
    B[c].add(d)
    B[d].add(c)
  D=[]
  #print(F)
  #print(B)
  ans=[0]*(N+1)
  main()