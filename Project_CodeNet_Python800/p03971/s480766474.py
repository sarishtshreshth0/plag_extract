n, a, b = map(int, input().split())
s = list(input())
line = a + b
rank = 1
bnum = 0
for student in s:
    if student == "a" or student== "b":
        if rank <= line:

            if student == "a":
                print("Yes")
                rank += 1
            else:
                bnum += 1
                if bnum <= b:
                    print("Yes")
                    rank += 1
                else:
                    print("No")
        else:
            print("No")
    else:
        # rank +=1
        print("No")