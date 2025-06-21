# XとYの二部グラフの最大マッチング X={0,1,2,...|X|-1} Y={0,1,2,...,|Y|-1}
#   edges[x]: xとつながるYの頂点のset
#   matched[y]: yとマッチングされたXの頂点(暫定)
 
def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False
 
 
# 標準入力からのグラフ読み取り
n = int(input())

r = [[0,0] for i in range(n)]
for i in range(n) :
  x,y = map(int,input().split())
  r[i][0],r[i][1] = x,y
  
b = [[0,0] for i in range(n)]
for i in range(n) :
  x,y = map(int,input().split())
  b[i][0],b[i][1] = x,y

edges = [set() for _ in range(n)]
matched = [-1] * n
  
for i in range(n) :
  for j in range(n) :
    if r[i][0] < b[j][0] and r[i][1] < b[j][1] :
      edges[i].add(j)
      
# 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる
print(sum(dfs(s, set()) for s in range(n)))