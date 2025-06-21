class UnionTree:

	# 節の数
	def __init__(self, N):
		self.__par = [i for i in range(N)]
		self.__rank = [0] * N

	# 根
	def root(self, x):
		if(self.__par[x] == x):
			return x
		else:
			self.__par[x] = self.root(self.__par[x])
			return self.__par[x]

	# 結合
	def unite(self, x, y):
		rx = self.root(x)
		ry = self.root(y)
		if(rx == ry):
			return

		if(self.__rank[rx] < self.__rank[ry]):
			self.__par[rx] = ry
		else:
			self.__par[ry] = rx
			if(self.__rank[rx] == self.__rank[ry]):
				self.__rank[rx] += 1

	# 一致
	def same(self, x, y):
		rx = self.root(x)
		ry = self.root(y)
		if(rx == ry):
			return True
		
		
# N枚のカードとルール
N, M = map(int, input().split())

# UnionTree Class
union_tree = UnionTree(N)

# ルールの適応
for i in range(M):
	# 結合
	a, b, x = map(int, input().split())
	union_tree.unite(a-1, b-1)

# 個数のみ数える
cnt = set()

for i in range(N):
	cnt.add(union_tree.root(i))

print(len(cnt))