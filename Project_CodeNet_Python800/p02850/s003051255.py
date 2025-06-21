n = int(input())
ikeru = [[] for _ in range(n)]
for i in range(n-1):
	a, b = map(int, input().split())
	ikeru[a-1].append((b-1, i))

settansaku = set([])
setmada = {0}
listmada = [(0, None)]  #left: Vertex, right: Color
kouho = 1
num = [0 for _ in range(n-1)]

while kouho != 0:
	for i, cnt in listmada[:]:
		colors = {cnt}
		settansaku.add(i)
		setmada.remove(i)
		listmada.remove((i, cnt))
		kouho -= 1
		c = 0
		for k, j in ikeru[i]:
			if not k in setmada:
				if not k in settansaku:
					setmada.add(k)
					while True:
						if c not in colors:
							listmada.append((k, c))
							colors.add(c)
							num[j] = c
							break
						c += 1
					kouho += 1

print(max(num)+1)
print("\n".join([str(i+1) for i in num]))