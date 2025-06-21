def solve():
    N = int(input())
    S = input()
    l,r = 0,0
    state = 'r'
    for i in range(N):
        if i == 0 and S[i] == ')': state = 'l'
        # if S[i] == '(': state = 'r'
        if i > 0  and S[i-1] == ')' and S[i] == '(':
            state = 'r' 
            
        if S[i] == '(':
            if state == 'l':
                if l > 0:
                    l -= 1
                else:
                    r += 1
            elif state == 'r':
                r += 1
        elif S[i] == ')':
            if state == 'r':
                if r > 0:
                    r -= 1
                else:
                    l += 1
            elif state == 'l':
                l += 1
                
        # print(state,l,r)
            
    print('('*l+S+')'*r)
    
solve()