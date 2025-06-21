from collections import deque
n = int(input())
num753 = set()
q = deque([3,5,7])

#753数(準753も含む)の全列挙
while q:

    #右端の値を取り出す
    x = q.pop()

    #xが10**9以上になったら終了
    if x <= 10**9:

        #集合型のnum753にxを追加
        num753.add(x)

        #xを10倍して7,5,3をそれぞれ足した数をキューに追加
        q.append(x*10+3)
        q.append(x*10+5)
        q.append(x*10+7)
count = 0

#num753に格納してある値からn以下の753数を判定
for i in num753:
    if i <= n:
        lst = list(str(i))
        if "3" in lst and "5" in lst and "7" in lst:
            count += 1

print(count)