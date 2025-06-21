def main():
  n,m,k=map(int,input().split())
  ab=[list(map(int,input().split())) for _ in range(m)]
  cd=[list(map(int,input().split())) for _ in range(k)]
  friend=[set()for _ in range(n)]
  block=[set()for _ in range(n)]
  for a,b in ab:
    friend[a-1].add(b-1)
    friend[b-1].add(a-1)
  for c,d in cd:
    block[c-1].add(d-1)
    block[d-1].add(c-1)
  # 友達連結内でかつ友達でもブロックでもない。
  # 友達連結グループわけ
  ans=[0]*n
  seen=[0]*n
  for t in range(n):
    if seen[t]==1:
      continue
    member=set()
    todo=[t]
    seen[t]=1
    while todo:
      t=todo.pop()
      member.add(t)
      f=friend[t]
      for fi in f:
        if seen[fi]==0:
          todo.append(fi)
          seen[fi]=1
    mn=len(member)
    for m in member:
      ans[m]=mn-len(block[m].intersection(member))-len(friend[m])-1
  print(' '.join(map(str,ans)))
if __name__=='__main__':
  main()
