s=list(input())
id_1=['1' if i%2 else '0' for i in range(len(s))]
id_2=['0' if i%2 else '1' for i in range(len(s))]
cnt=[0,0]
for si,id1,id2 in zip(s,id_1,id_2):
  cnt[0] += si!=id1
  cnt[1] += si!=id2
print(min(cnt))