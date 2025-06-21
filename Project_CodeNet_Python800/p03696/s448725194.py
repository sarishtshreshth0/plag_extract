import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

n = ni()
s = ns().strip()
h = 0
minh = 0
for c in s:
    if c == "(":
        h += 1
    else:
        h -= 1
    minh = min(minh, h)
print("("*(-minh) + s + ")"*(h-minh))
#括弧列では、任意の接頭辞で、"("の方が多いこと、かつ全体で(と)の数が等しいことが必要なので、そうなる条件を考える。
#一番バランスが悪いところに合わせて(を先頭からならべ、後方に)を並べて整合性を取ればよく、その方法が辞書順最小であることが示される(解説参照)
#括弧列に関してあまり考えずに逆算してしまった。
