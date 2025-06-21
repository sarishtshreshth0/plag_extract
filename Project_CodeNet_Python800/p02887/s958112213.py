N =int(input())
S =input()
counter = 1
for i in range(1,N):
    if S[i] != S[i-1]:
        counter += 1
print(counter)
