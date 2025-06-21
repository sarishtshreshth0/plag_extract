n = int(input())
word = input()
answer = 0
for i in range(n-1):
    if word[i] != word[i+1]:
        answer += 1
print(answer+1)