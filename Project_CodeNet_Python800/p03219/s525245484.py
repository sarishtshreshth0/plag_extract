# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
X,Y = (int(i) for i in input().split())
ans =X +Y//2
print(ans)