n = list(input())
denominator_ = sum( list(map(int, n)) )
molecule____ = int( "".join(n) )
if molecule____ % denominator_ == 0:
    print("Yes")
else:
    print("No")
