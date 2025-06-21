#!/usr/bin/env python
import os
import operator
import sys
from io import BytesIO, IOBase

def inar():
    return [int(k) for k in input().split()]
def main():
    s=input()
    t=input()
    dp=[]
    arrow=[]
    for i in range(len(t)+1):
        lis=[0 for k in range(len(s)+1)]
        lis1=["" for l in range(len(s)+1)]
        dp.append(lis)
        arrow.append(lis1)
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
            if t[i-1]==s[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                arrow[i][j]="C"
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    dp[i][j]=dp[i][j-1]
                    arrow[i][j]="L"
                else:
                    dp[i][j]=dp[i-1][j]
                    arrow[i][j]="U"
    res=""
    i=len(t)
    j=len(s)
    # for i in range(len(t)+1):
    #     print(*arrow[i])
    while 1:
        if i==0 or j==0:
            break
        if arrow[i][j]=="C":
            res+=s[j-1]
            i-=1
            j-=1
        elif arrow[i][j]=="U":
            i-=1
        else:
            j-=1
    print(res[::-1])



BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()