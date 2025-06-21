import re
A, B = map(int,input().split())
S = input()
m = '^[0-9]{' + str(A) + '}-[0-9]{' + str(B) +'}$'
if re.match(m, S):
    print("Yes")
else:
    print("No")