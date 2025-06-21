N = int(input())
S = str(input())
#print(N,S)

stack = []
while len(S) > 0:
    if len(stack) == 0:
        stack.append(S[0])
        S = S[1:]
    elif S[0] == stack[-1]:
        S = S[1:]
    
    elif S[0] != stack[-1]:
        stack.append(S[0])
        S = S[1:]
    #print(S,stack)
print(len(stack))
        
