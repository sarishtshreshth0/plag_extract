# 回答を読んで作成
# 全体の半分に到達可能、ただし１行もしくは１列の時は動けない
h,w = map(int, input().split())
if h==1 or w==1:
  ans = 1
else:
  ch = (h*w)/2
  ans = (ch//1)+((h*w)%2)
print(int(ans))