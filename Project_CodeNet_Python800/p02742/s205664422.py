import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

H, W = ri_()
if H == 1 or W == 1:
    print(1)
else:
    print(-(-H * W // 2))