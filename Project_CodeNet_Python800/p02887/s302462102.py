

n = int(input())

s = input()


count = 1



for h in range(len(s)-1):
 
    if s[h] != s[h+1]:
        count += 1

print(count)

