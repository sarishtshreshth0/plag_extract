import sys
import fractions
input = sys.stdin.readline
N = int(input())
print(int(2 * N/(fractions.gcd(2, N))))