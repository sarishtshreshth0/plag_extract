N = int(input())
from collections import deque
def main():
    ans = 0
    targets = deque()
    targets.append('3')
    targets.append('5')
    targets.append('7')
    while targets:
        s = targets.popleft()
        if int(s) <= N:
            if '3' in s and '5' in s and '7' in s:
                ans += 1
            targets.append(s+'3')
            targets.append(s+'5')
            targets.append(s+'7')

    print(ans)
main()

        



