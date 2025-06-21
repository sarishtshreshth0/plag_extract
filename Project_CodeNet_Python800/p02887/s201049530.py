n = int(input())
s = input()

count = 1
i = 0

while i < n-1:
    if s[i] == s[i+1]:
        i += 1

    else:
        count += 1
        i += 1

print(count)