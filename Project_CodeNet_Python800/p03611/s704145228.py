N = int(input())
A = list(map(int, input().split()))

cnt=dict()
# a内の数とその±1をdict型の配列に入れながら個数をカウント
for a in A:
  cnt[a] = cnt.setdefault(a,0) + 1
  cnt[a-1] = cnt.setdefault(a-1,0) + 1
  cnt[a+1] = cnt.setdefault(a+1,0) + 1
  
  
# カウントした数字で昇順にソート  
cnt_sort = sorted(cnt.items(), key=lambda x:x[1])
cnt_sort.reverse()

print(cnt_sort[0][1])