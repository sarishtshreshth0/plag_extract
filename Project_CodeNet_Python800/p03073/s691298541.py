S = input()
L = [i&1 for i in range(len(S))]
m = sum(int(S[i])!=L[i] for i in range(len(S)))
print(m if m<=len(S)//2 else len(S)-m)