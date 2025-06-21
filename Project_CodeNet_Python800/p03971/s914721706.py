n ,a, b  =map(int, input().split())
S = list(input())
threshold = a + b
rank = 1
bnum = 1
for p in S:
    if p == "a" or p == "b":
        if rank <= threshold:
            if p == "b" and bnum <= b:
                print("Yes")
                bnum += 1
                rank += 1
            elif p == "b" and bnum > b:
                print("No")
                bnum += 1
            else:
                print("Yes")
                rank += 1
        else:
            print("No")
    else:
        print("No")