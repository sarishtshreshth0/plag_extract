X = int(input())

ureshi = 0

# 500 yen
ureshi += (X // 500) * 1000
X = X % 500

# 5 yen
ureshi += (X // 5) * 5

print(ureshi)