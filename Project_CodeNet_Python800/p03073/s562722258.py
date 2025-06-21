S = str(input())
if len(S) == 1:
    print(0)
    exit()
if len(S) % 2 == 0:
    ans1 = "10" * (len(S)//2)
    ans2 = "01" * (len(S)//2)
else:
    ans1 = "10" * (len(S)//2) + "1"
    ans2 = "01" * (len(S)//2) + "0"

result1 = 0
result2 = 0
for x,y in zip(S,ans1):
    if x != y:
        result1 += 1
for x,y in zip(S, ans2):
    if x != y:
        result2 += 1
print(min(result1,result2))
    
