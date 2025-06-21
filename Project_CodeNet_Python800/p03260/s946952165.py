#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
A,B = inputlist()
if A % 2 == 1 and B % 2 == 1:
    print("Yes")
else:
    print("No")