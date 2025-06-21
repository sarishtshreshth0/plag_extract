N = int(input())
S = input()

counter = 0
past = S[0]
for s in S[1:]:
    
    if not s==past:
        counter += 1
        past = s
    
print(counter+1)