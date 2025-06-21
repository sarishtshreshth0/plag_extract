N, A, B = map(int, input().split())
S = list(input())

answer = 0
b_list = 0
for idx, moji in enumerate(S):
    if moji == "a" and answer < A + B:
        answer += 1
        print("Yes")
        continue
    elif moji == "b":
        b_list += 1
        if answer < A + B and b_list <= B:
            answer += 1
            print("Yes")
            continue
    print("No")
