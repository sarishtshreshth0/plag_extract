N=int(input())
S = input()
List = list(S)
resList = [S[0]]
for i in range(1,N):
  if List[i] == List[i-1]:
    pass
  else:
    resList.append(List[i])
print(len(resList))