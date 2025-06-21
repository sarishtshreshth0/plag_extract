#C - Coloring Colorfully
S = list(input())
S_rev = list(reversed(S))
if len(S) == 1:
    count_min = 0
else:    
    count_front = 0
    for i in range(1,len(S)):
        if S[i] == S[i-1] == '1':
            S[i] = '0'
            count_front += 1
        elif S[i] == S[i-1] == '0':
            S[i] = '1'
            count_front += 1
    count_back = 0
    for j in range(1,len(S)):
        if S_rev[j] == S_rev[j-1] == '1':
            S_rev[j] = '0'
            count_back += 1
        elif S_rev[j] == S_rev[j-1] == '0':
            S_rev[j] = '1'
            count_back += 1
    count_min = min(count_front,count_back)
print(count_min)