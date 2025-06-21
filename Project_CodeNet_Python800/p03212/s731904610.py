n=int(input())
num=["3","5","7"]
l=["0"]#pythonの仕様上、初期値は"0"
i=0
while True:#3,5,7のどれかのみを含む値を文字列としてlに追加していく
    for j in num:
        l.append(l[i]+j)
    i+=1
    if len(l[-1])==11:
        break
#print(l)
L=[]
for j in range(len(l)):#3,5,7をそれぞれ１つ以上含むものだけを整数型にしてLに収納
    if "3" in l[j] and "5" in l[j] and "7" in l[j] and int(l[j])<10**9:
        L.append(int(l[j]))
L.sort()
#print(L)
ans=0
for k in range(len(L)):
    if L[k]<=n:
        ans+=1
    else:
        break
print(ans)