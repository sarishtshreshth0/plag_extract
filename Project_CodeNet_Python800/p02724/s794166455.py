X = int(input())

happiness = 0
X_remaining = X

happiness = happiness + (int(X_remaining / 500)*1000)
X_remaining = X_remaining % 500

happiness = happiness + (int(X_remaining / 5)*5)

print(happiness)