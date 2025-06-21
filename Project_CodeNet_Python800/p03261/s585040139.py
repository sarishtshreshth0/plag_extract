#https://atcoder.jp/contests/abc109/tasks/abc109_b
import collections
N = int(input())
Word_List = []
SP = ""
for i in range(N):
    CW = str(input())
    if i == 0:
        Word_List.append(CW)
        SP = CW[-1]
    elif SP != CW[0]:
        print("No")
        break
    else:
        Word_List.append(CW)
        SP = CW[-1]
else:
    Word_List = collections.Counter(Word_List)
    if len(Word_List) != N:
        print("No")
    else:
        print("Yes")