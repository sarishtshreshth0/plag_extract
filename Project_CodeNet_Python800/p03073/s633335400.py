S = input()
N = S[::2].count("0")+S[1::2].count("1")
print(min(N,len(S)-N))