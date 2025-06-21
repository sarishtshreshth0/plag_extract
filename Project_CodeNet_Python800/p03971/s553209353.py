import sys
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7

n, a, b = LI()
s = S()

# n人が参加するコンペに国内の学生か海外の学生かその他がいる。
# 国内または海外の学生のみが予選通過でき、上位の学生から以下の条件を満たすとき通過
# 国内の学生は通過確定した参加者がA+B人に満たなければ通過
# 海外の学生は通過確定した参加者がA+B人に満たず、海外の学生中での順位がB位以内ならば予選通過

# Sは参加者の情報を示す文字列。i番目の文字がaの時予選i位の参加者が国内の学生、bの時は海外の学生。
# cの時はその他。
# すべての参加者に対して予選通過に対しYes、Noを出力せよ

sl = list(s)
list_a = []
list_b = []
max_pass = a + b

for i in range(len(sl)):
    if sl[i] == "a":
        if len(list_a) + len(list_b) < max_pass:
            sl[i] = "Yes"
            list_a.append(i)
        else:
            sl[i] = "No"
    elif sl[i] == "b":
        if len(list_a) + len(list_b) < max_pass and len(list_b) < b:
            sl[i] = "Yes"
            list_b.append(i)
        else:
            sl[i] = "No"
    elif sl[i] == "c":
        sl[i] = "No"

for x in sl:
    print(x)
