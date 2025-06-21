# 空白区切り
x, y = map(int, input().split())
# 改行区切り
# s = int(input())

# 鉄道 A -> B : X円
# バス B -> C : Y円

# X:10円 Y:100円
ans = x + (y / 2)
print(int(ans))
