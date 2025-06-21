N, A, B = map(int,input().split(" "))
S = input()
count = {"a":0,"b":0}
for s in S:
    if s == "a" and count["a"] + count["b"] < A+B:
        count["a"] += 1
        print("Yes")
    elif s == "b" and count["a"] + count["b"] < A+B and count["b"]<B:
        count["b"]+=1
        print("Yes")
    else:
        print("No")