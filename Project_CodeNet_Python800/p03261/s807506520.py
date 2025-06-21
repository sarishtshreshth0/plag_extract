N=int(input())
H=input()
word=[]
word.append(H)
for i in range(N-1):
  S=input()
  if S in word:
    print('No')
    exit()
  else:
    if H[-1]==S[0]:
      H=S
      word.append(H)
    else:
      print('No')
      exit()
print('Yes')