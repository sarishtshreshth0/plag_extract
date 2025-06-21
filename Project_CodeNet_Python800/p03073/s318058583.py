s = str(input())

# print(s)
count =0
for xi in range(len(s)):
    if xi%2 ==0:t="0"
    if xi%2 ==1:t="1"

    if s[xi]==t:
        count+=1

# print(count)
print(min(count,len(s)-count))
