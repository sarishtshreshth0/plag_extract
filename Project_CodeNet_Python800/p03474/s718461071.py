def main():
    A, B = map(int, input().split())
    S = str(input())
    f = 0
    
    for i in range(A):
        if S[i].isnumeric():
            continue
        else:
            print('No')
            return
    
    if S[A] != '-':
        print('No')
        return
    
    for i in range(A+1, A+B+1):
        if S[i].isnumeric():
            continue
        else:
            print('No')
            return
    print('Yes')
    
main()