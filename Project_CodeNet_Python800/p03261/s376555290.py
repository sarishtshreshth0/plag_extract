N = int(input())
lis = []

for i in range(N):
    s = input()
    if i == 0:
        end_w = s[0]

    if s in lis:
        print("No")
        exit()
    else:
        if s[0] == end_w:
            lis.append(s)
            end_w = s[-1]
        else:
            print("No")
            exit()

print("Yes")
