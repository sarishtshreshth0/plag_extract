from sys import stdin

def readString() :
    return  stdin.readline().rstrip()

def solve() :
    S = readString()
    pos = S.find('YAKI')
    if(pos == 0) :
        print("Yes")
    else :
        print("No")
solve()