n = int(input())

def ct(s):
    count = 0
    if int(s) > n:
        return count
    if all(s.count(i) > 0 for i in '753'):
        count += 1
    for i in '753':
        count += ct(s + i)
    return count

print(ct('0'))
