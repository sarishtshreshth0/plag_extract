import sys
N = int(input())
array_word = [ input() for word in range(N) ]

before = array_word[0]
for I in array_word[1:]:
    if before[-1] == I[0] and array_word.count(I) == 1:
        before = I
        continue 
    else:
        print('No')
        sys.exit()
print('Yes')