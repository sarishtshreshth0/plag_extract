import sys

def main(lines):
  a, b = map(int, lines[0].split())
  if a % 2 != 0 and b % 2 != 0:
    print("Yes")
    return
  print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)