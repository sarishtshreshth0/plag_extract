def main():
    N = int(input())
    S = input()
    fusion = [S[0]]
    prev = S[0]
    for s in S[1:]:
        if s == prev:
            continue
        fusion.append(s)
        prev = s
    print(len(fusion))
main()