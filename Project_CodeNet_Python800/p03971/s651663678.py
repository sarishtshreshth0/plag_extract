N,A,B = map(int,input().split())
S = str(input())
now = 0
kaigai = 0
for i in range(N):
  temp = S[i]
  if temp == "a" and now < A+B:
    print("Yes")
    now +=1
  elif temp == "b" and now < A+B and kaigai < B:
    print("Yes")
    kaigai += 1
    now += 1
  else:
    print("No")