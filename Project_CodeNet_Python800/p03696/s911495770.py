import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import chain
def main():
    n = int(input())
    s = tuple(input())
    cnt = 0
    cnt_ushiro = 0
    cnt_mae = 0
    for se in s:
        cnt += se == ')'
        cnt -= se == '('
        cnt_mae = max(cnt_mae, cnt)
    cnt -= cnt_mae
    if cnt < 0:
        cnt_ushiro = -cnt
    s_mae = ('(') * cnt_mae
    s_ushiro = (')') * cnt_ushiro
    r = tuple(chain(s_mae, s, s_ushiro))
    print(*r,sep="")

if __name__ == '__main__':
    main()