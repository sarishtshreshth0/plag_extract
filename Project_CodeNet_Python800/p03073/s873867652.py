S = input()
n = S[::2].count('0')+S[1::2].count('1')
print(min(n, len(S)-n))
