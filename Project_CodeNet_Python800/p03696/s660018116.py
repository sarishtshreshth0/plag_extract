def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    S = input()
    par = [0]
    cc = 0
    for i in S:
        if i == '(': cc += 1
        else: cc -= 1
        par.append(cc)

    mp = min(par)
    output = S
    if mp < 0: output = '(' * abs(mp) + output
    if abs(mp) + cc > 0: output = output + ')' * (abs(mp)+cc)
    print(output)

    return

if __name__ == '__main__':
    main()
