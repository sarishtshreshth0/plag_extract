import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = input()
cnt1 = 0
for i, j in enumerate(s):
    if (i+1)&1:
        if j=='1':
            cnt1 += 1
    else:
        if j=='0':
            cnt1 += 1

print(min(cnt1, len(s)-cnt1))