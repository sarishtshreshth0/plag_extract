n = input()
s = input()
# n：スライムの数
# s：スライムの色情報

# 最終的に存在するスライムの数を答える
judge_str = s[0]
ans=1
for i in s:
    if i != judge_str:
        ans+=1
        judge_str = i
print(ans)