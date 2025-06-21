import collections
N=int(input())
D=list(map(int,input().split()))
l=[]
c=collections.Counter(D)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
p=998244353
cnt=1
for i in range(len(key)):
    l.append([key[i],values[i]])#lは[要素i,n_i]の情報を詰めたmatrix
#print(l)
if (c[0]==1)and(D[0]==0):
    for i in range(N-1):
        cnt=cnt*pow(c[i],c[i+1],p)
    print(cnt%p)
else:
    print("0")