input()
S=input()
print(1+sum(S[i]!=S[i+1]for i in range(len(S)-1)))