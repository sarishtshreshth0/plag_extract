def judge_passing_qualifying_domestic(i, line):
    if i < A+B:
        print('Yes')
        return i+1
    else:
        print('No')
        return i

def judge_passing_qualifying_foreign(i, rank_in_foreign, line, line_foreign):
    if (i < A+B)&(rank_in_foreign <= line_foreign):
        print('Yes')
        return i+1, rank_in_foreign+1
    else:
        print('No')
        return i, rank_in_foreign+1


if __name__ == "__main__":
    N, A, B = list(map(int, input().split()))
    S = input()
    num_of_pass = 0
    rank_in_foreign = 1
    for p in list(S):
        if p == 'a':
            num_of_pass = judge_passing_qualifying_domestic(num_of_pass, A+B)
        elif p =='b':
            num_of_pass, rank_in_foreign = judge_passing_qualifying_foreign(num_of_pass, rank_in_foreign, A+B, B)
        else:
            print('No')