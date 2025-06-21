from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    b.append(i + 1)
    b.append(i)
    b.append(i - 1)
##辞書型 キーに要素、値に出現回数を出力
c = Counter(b)
##most_comonn (要素, 出現回数)という形のタプルを出現回数順に並べたリストを返す
##出現回数が最も多いものは[0],出現回数のみを出力するので[1]
print(c.most_common()[0][1])
