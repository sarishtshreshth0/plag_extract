import numpy as np
import math
from collections import Counter

def cumsum(x):
    return list(np.cumsum(x))

def cumsum_number(N,K,x):
    ans=[0]*(N-K+1)
    number_cumsum = cumsum(x)
    number_cumsum.insert(0,0)
    for i in range(N-K+1):
        ans[i]=number_cumsum[i+K]-number_cumsum[i]
    return ans
"""
int #整数
float #小数

#リスト
list0 = [] #リスト生成
list0 = [1,2,3,4] #初期化
list0 = [0]*10 #[0,0,0,0,0,0,0,0,0,0]
list1= [i for i in range(10)] #>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = list(map(int, input().split()))　# 複数の入力をリストに入れる
number=[int(input()) for i in range(int(input()))] #複数行の入力をリストに
list1 = list1 + [6, 7, 8] #リストの追加
list2.append(34) #リストの追加　最後に（）内が足される
list.insert(3,10) #リストの追加　任意の位置（追加したい位置,追加したい値）
len(list4) #リストの要素数
max(sa) #list saの最小値
list5.count(2) #リスト(文字列も可）内の2の数
list1.sort() #並び替え小さい順
list1.sort(reverse=True)  #並び替え大きい順
set(list1) #list1内の重複している要素を削除し、小さい順に並べる
sum([2,3,   ,3]) #リストの合計

number=Counter(list) #listを値（文字）ごとにカウントし辞書型で返す [1:4,2:5 …]

abs(a) #aの絶対値
max(a,b) min(a,b) #最大値　最小値
text1 = text1.replace("34","test") #text1内の"34"を"test"に書き換える(文字列内の文字を入れ替える)
sorted(S) #Sを辞書順にソート
exit(0) #強制終了

cumsum(リスト) #累積和をリストで返す
cumsum_number(N,K,x) #N個の数が含まれるリストx内のK個からなる部分和をリストで返す

alphabet={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",
          10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",
          20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z",}
print(*S,sep="") #リストSを1つずつ出力

math.floor() #切り捨て
math.ceil() #切り上げ
"""
def dist(a,b):
    res = 0
    for i in range(D):
        res += (a[i]-b[i])**2
    res = res**0.5
    return res

N,D=map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        if dist(X[i],X[j]).is_integer():
            ans+=1
print(ans)




