import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
words = lines
prev_last_char = None
words_already_used = {}
for w in words:
    if w in words_already_used:
        print("No")
        break
    else:
        words_already_used[w] = True
    if prev_last_char is not None:
        if w[0] != prev_last_char:
            print("No")
            break
    prev_last_char = w[-1]
else:
    print("Yes")
