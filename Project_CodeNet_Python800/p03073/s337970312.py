#from distutils.util import strtobool
s = input()
ss = [int(s[0]) if x % 2 == 0 else int(s[0])^1 for x in range(len(s))]

cnt = 0
for i in range(len(s)):
    if int(s[i]) != ss[i]:
        cnt += 1

print(cnt)