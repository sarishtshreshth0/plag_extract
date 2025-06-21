N = int(input())
#print(N)

S = input()

count = 0
for i in range(N):
    #print(S[i] , i)
    if i == N-1:
        break
    else:
        if S[i+1] != S[i]:
            count += 1

if count == 0:
    print(1)
else:
    print(count+1)