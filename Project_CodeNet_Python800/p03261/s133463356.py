# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
N = int(input())
w =[]
for i in range(N):
    x =input().strip()
    w.append(x)

#重複回答チェック
from collections import Counter
c =Counter(w)
c_k =list(c.values())
ans =""
if max(c_k) >=2:
    print("No")
    sys.exit()
    
ans ="Yes"
for i in range(N-1):
    if w[i][-1] != w[i+1][0]:
        ans ="No"
        break
print(ans)
