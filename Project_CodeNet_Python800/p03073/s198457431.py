S = input()
SE = S[::2]
SO = S[1::2]
print(min(SE.count('1')+SO.count('0'), SE.count('0')+SO.count('1')))
