n, a, b = map(int, input().split(' '))
s = input()

passed_count = 0
passed_count_foreigner = 0

for person in s:
    if passed_count < a + b and person == "a":
        print("Yes")
        passed_count += 1
    elif passed_count < a + b and person == "b" and passed_count_foreigner < b:
        print("Yes")
        passed_count += 1
        passed_count_foreigner += 1
    else:
        print("No")