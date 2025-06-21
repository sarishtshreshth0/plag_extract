import itertools
import fractions
def main():
  n = int(input())
  a = fractions.gcd(2,n)#gcd = 最大公約数
  lcm = 2 * n//a#lcm 最小公倍数
  print(lcm)
if __name__ == '__main__':
  main()