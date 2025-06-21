def resolve():
    a, b, c = map(int, input().split())
    print("Yes" if sorted([a, b, c])[1] == c else "No")


if __name__ == "__main__":
    resolve()
