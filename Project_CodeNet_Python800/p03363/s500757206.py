import collections
N=int(input())
A=list(map(int,input().split()))
l=[0]
l2=[]
for i in range(N):
    l.append(l[len(l)-1]+A[i])
#print(l)
ans=0
c=collections.Counter(l)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
for i in range(len(key)):
    l2.append([key[i],values[i]])#lは[要素i,n_i]の情報を詰めたmatrix
for i in range(len(key)):
    ans=ans+(l2[i][1]*(l2[i][1]-1))//2
print(ans)