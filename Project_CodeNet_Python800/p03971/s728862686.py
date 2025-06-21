# ####################################################################
# import io
# import sys

# _INPUT = """\
# 12 5 2
# cabbabaacaba

# 10 2 3
# abccabaabb
# """
# sys.stdin = io.StringIO(_INPUT)
####################################################################
import sys
def p(*_a):
  return
  _s=" ".join(map(str,_a))
  #print(_s)
  sys.stderr.write(_s+"\n")
####################################################################
yn = lambda b: print('Yes') if b else print('No')
####################################################################

N,A,B = map(int, input().split())
S = input()

a = b = 0

for s in S:
  p("   ",A,B,A+B,"_",s, a,b, a+b)
  if s == 'a':
    if (a+b) < (A+B):
      yn(True)
      a += 1
    else:
      yn(False)
  elif s == 'b':
    if ((a+b) < (A+B)) and (b < B):
      yn(True)
      b += 1
    else:
      yn(False)
  elif s == 'c':
    yn(False)

