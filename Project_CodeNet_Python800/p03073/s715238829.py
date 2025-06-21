s=input()

#0はじまりの場合
ans_0=0
count=0
for i in s:
    if int(i) != count % 2: ans_0+=1
    count+=1

#1はじまりの場合
ans_1=0
count=1
for i in s:
    if int(i) != count %2: ans_1+=1
    count+=1

print(min(ans_0,ans_1))