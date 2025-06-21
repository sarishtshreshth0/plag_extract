N = int(input())
S = input()
total,min_total = 0, 1
for s in S:
    total += 1 if s == '(' else -1
    if total < min_total:
        min_total = total    
print('('*-min_total+S+')'*(total-min_total) if min_total<0 else S+')'*total)