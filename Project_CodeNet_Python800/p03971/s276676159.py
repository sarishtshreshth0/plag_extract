_,A,B = map(int,input().split())
s = list(input())

ab = 0
b = 0

for i in s:
    res = "No"
    
    if i == "a":
        if ab < A+B:
            ab += 1
            res = "Yes"
            
    if i == "b":
        if ab < A+B and b < B:
            ab += 1
            b += 1
            res = "Yes"
            
    print(res)