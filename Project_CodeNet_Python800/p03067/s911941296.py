import sys
import math
import bisect

def main():
    a, b, c = map(int, input().split())
    a, b = min(a, b), max(a, b)
    if c >= a and c <= b:
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()
