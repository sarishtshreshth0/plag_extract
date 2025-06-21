#54
import sys
N = int(input())
word = [] 

w = input()
word.append(w)

for i in range(N-1):
    w = input()
    if word[-1][-1] != w[0]:
        print("No")
        sys.exit()
    for j in word:
        if j == w:
            print("No")
            sys.exit()
    word.append(w)
    
print("Yes")