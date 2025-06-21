#B-Qualification simulator
N, A, B = map(int, input().split())
S = input()
a = 0
b = 0

for i in S:
    if i == "a":
        if a + b < A + B:
            print ("Yes")
            a += 1
        else:
            print ("No")
    elif i == "b":
        if (a + b <A + B) and (b < B):
            print ("Yes")
            b += 1
        else:
            print ("No")
    else:
        print ("No")
