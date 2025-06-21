H, W = map(int, input().split())

w1, w2 = W // 2, W % 2
h1, h2 = H // 2, H % 2

if H > 1 and W > 1:
	num = 2 * w1 * h1 + w2 * h1 + w1 * h2 + w2 * h2 
else:
  num = 1
print(num)

