n = int(input())
string = input()
start_cnt = 0
end_cnt = 0
tmp = 0
for s in string:
    if s == ")":
        if tmp == 0:
            start_cnt += 1
        else:
            tmp -= 1
    else:
        tmp += 1
tmp = 0
for s in string[::-1]:
    if s == "(":
        if tmp == 0:
            end_cnt += 1
        else:
            tmp -= 1
    else:
        tmp += 1
for _ in range(start_cnt):
    print("(", end = "")
    
print(string, end = "")

for _ in range(end_cnt):
    print(")", end = "")
    
print()