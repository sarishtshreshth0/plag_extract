from collections import deque

def main():
    N = int(input())
    S = list(input())
    Stmp = S.copy()
    Stmp = deque(Stmp)
    cnt = 0
    for s in S:
        cnt += (s=='(') - (s==')')
        if cnt < 0:
            Stmp.appendleft('(')
            cnt += 1
    for _ in range(cnt):
        Stmp.append(')')
    print(''.join(Stmp))

if __name__ == "__main__":
    main()
