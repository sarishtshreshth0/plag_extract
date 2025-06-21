def main():
    N = input_int()
    S = input()

    validitylist = [False] * N
    validitylist[0] = True

    for i in range(1, N):
        if S[i-1] != S[i]:
            validitylist[i] = True
    
    print(len([i for i in validitylist if i is True]))



def input_int():
    return int(input())


def input_int_tuple():
    return map(int, input().split())


def input_int_list():
    return list(map(int, input().split()))


main()
