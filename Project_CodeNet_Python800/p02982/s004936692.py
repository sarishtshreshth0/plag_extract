# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
import math

def resolve():
    import sys
    input = sys.stdin.readline
    n, d = [int(x) for x in input().rstrip().split(" ")]

    ans = 0
    points = []

    for i in range(n):
        current = [int(x) for x in input().rstrip().split(" ")]
        for point in points:
            dist = math.sqrt(sum([(a - b)**2 for a, b in zip(point, current)]))
            if dist.is_integer():
                ans += 1
        points.append(current)

    print(ans)



if __name__ == "__main__":
    resolve()
