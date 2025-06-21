n,a,b = map(int, input().split())
s = str(input())

counter1 = counter2 = 1
for char in s:
    if (counter1 <= (a+b)) & (char == 'a'):
        print("Yes")
        counter1 += 1
    elif (counter1 <= (a+b)) & (char == 'b') & (counter2 <= b):
        print("Yes")
        counter1 += 1
        counter2 += 1
    else:
        print("No")