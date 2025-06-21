N, A, B = map(int, input().split())
S = input()

passing_count = 0
rank = 1
for s in S:
    if s in ["a", "b"]:
        if passing_count < A + B:
            if s == "a":
                print("Yes")
                passing_count += 1
                continue
            else:
                if rank <= B:
                    print("Yes")
                    passing_count += 1
                    rank += 1
                    continue
    print("No")