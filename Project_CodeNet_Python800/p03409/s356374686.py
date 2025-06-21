N = int(input())
red = []
for i in range(N):
    a, b = map(int, input().split())
    red.append((a, b))
red = sorted(red, key=lambda x: (x[1]), reverse=True)
# print(red)

blue = []
for i in range(N):
    a, b = map(int, input().split())
    blue.append((a, b))
blue = sorted(blue, key=lambda x: (x[0], x[1]))
# print(blue)

count = 0
for i in range(N):
    b = blue[i]
    # print("{}".format(b))
    for j in range(len(red)):
        r = red[j]
        # print("{}".format(r))
        if r[0] < b[0] and r[1] < b[1]:
            # print("{}:{}".format(b, r))
            count += 1
            red.pop(j)
            break

print(count)
