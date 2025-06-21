# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
A,B = map(int, input().split())
ans ="No"
for i in range(1,4):
    if A*B*i %2 ==1:
        ans ="Yes"
        break
print(ans)