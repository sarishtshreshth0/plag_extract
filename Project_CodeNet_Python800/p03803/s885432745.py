# coding: utf-8

a, b = map(int,input().split())
l = [i for i in range(2,14)]
l.append(1)

ia = l.index(a)
ib = l.index(b)
def p(s):
    print(s)
if ia > ib:
    p("Alice")
elif ia < ib:
    p("Bob")
else:
    p("Draw")