import math
from math import fabs
def main(inp1, inp2, X):
    FinalValue = 0
    for all in range(inp1+1):
        for iterater in range(all + 1, inp1):
            var = 0.0
            for rangeinp2 in range(inp2):
                var += fabs( (int(X[all][rangeinp2]) - int(X[iterater][rangeinp2]))**2 )
            var = var ** 0.5
            varint=int(var)
            if var==varint:
                FinalValue += 1
    return FinalValue
inp1, inp2 = map(int, input().split())
X = [input().split() for _ in range(inp1)]
print(main(inp1, inp2, X))