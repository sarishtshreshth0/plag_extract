s = list(input())

length = len(s)
count = 0

for i in range(length-1):
    if i == length:
        break
    if s[i] == s[i+1]:
        if s[i] == '0':
            s[i+1] = '1'
            count += 1
        else:
            s[i+1] = '0'
            count += 1


print(count)