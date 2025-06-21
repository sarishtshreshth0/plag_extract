N = int(input())
S = input()
S_ = []

for i in range(len(S)-1):
    if i == len(S)-2 and S[i] != S[i+1]:
        S_.append(S[i])
        S_.append(S[i+1])
    elif i == len(S)-2 and S[i] == S[i+1]:
        S_.append(S[i])
    elif S[i] != S[i+1]:
        S_.append(S[i])
if len(S_) == 0:
    print('1')
else:
    print(len(S_))
    
