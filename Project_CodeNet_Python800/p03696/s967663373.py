n = int(input())
s = input()

data = [0, 0]  # [, ] = num of ( and )
temp = -1
for i in range(n):
    temp += 1
    tar = s[temp]
    if (tar == '('):
        data[0] += 1

    else:
        if (data[0] > data[1]):
            data[0] -= 1
        else:
            s = '(' + s
            temp += 1


add = ')' * data[0]
s = s + add

print(s)
