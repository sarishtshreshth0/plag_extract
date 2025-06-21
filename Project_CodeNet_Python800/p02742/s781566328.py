#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	H, W = getlist()
	if H == 1 or W == 1:
		print(1)
		return

	if (H * W) % 2 == 0:
		print(int(H * W // 2))
		return

	print((H * W // 2) + 1)


if __name__ == '__main__':
	main()