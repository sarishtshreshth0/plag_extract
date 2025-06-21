N = int(input())

def func(cur, use, counter):
	#今の値がNより大きければ処理をやめる
	if cur > N:
		return
	#現在の値が7, 5, 3を一つ以上使っていればカウンタを1増やす
	if use == 0b111:
		counter.append(1)

	#7を追加する
	func(cur*10+7, use | 0b001, counter)
	#5を追加する
	func(cur*10+5, use | 0b010, counter)
	#3を追加する
	func(cur*10+3, use | 0b100, counter)

res = []
func(0, 0, res)
print(sum(res))