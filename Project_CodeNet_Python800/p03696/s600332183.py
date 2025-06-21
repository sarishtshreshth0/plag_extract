N = int(input())
S = input()

dic = {'(':1, ')':-1}

rlt = ''
cnt = 0
for s in S:
  cnt += dic[s]
  rlt += s
  if cnt < 0:
    rlt = '(' + rlt
    cnt = 0
  
if cnt > 0:
  rlt += ')'*cnt
  
print(rlt)