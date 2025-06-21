# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない

#直積その 2 列挙
from itertools import product
N =input().strip()
N_int =int(N)
count =0
for i in range(3,len(N)+1):
    for tt in product(["3","5","7"], repeat=i):
        t ="".join(tt)
        if t.count("3") >=1 and t.count("5") >=1 and t.count("7") >=1 and int(t) <=N_int:
            count +=1
            #print(t,end=" ")
print(count)