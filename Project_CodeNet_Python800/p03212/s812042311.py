N = int(input())

list753 = [3, 5, 7]
beforeLength = 0
for i in range(1, 9):
    afterLength = len(list753)
    for j in range(3):
        for k in range(beforeLength, afterLength):
            x = list753[k] + 10 ** i * list753[j]
            list753.append(x)
    beforeLength = afterLength

listTrue753 = []
for i in list753:
    numberString = str(i)
    if numberString.count("3") > 0 and numberString.count("5") > 0 and numberString.count("7"):
        listTrue753.append(i)

count = 0
for i in listTrue753:
    if i <= N:
        count += 1
print(count)