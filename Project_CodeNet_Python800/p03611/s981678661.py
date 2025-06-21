import collections as c
input();a1=list(map(int,input().split()));a2,a3=[i-1 for i in a1],[i+1 for i in a1]
print(c.Counter(c.Counter(a1)+c.Counter(a2)+c.Counter(a3)).most_common(1)[0][1])