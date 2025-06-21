N, A, B = map(int, input().split(' '))
S = list(input())

passed_num = 0
limit = A + B
ranking_foreign = 1

results = []

for examinee in S:
    if passed_num < limit:
        if examinee == 'a':
            passed_num += 1
            results.append('Yes')
        elif examinee == 'b':
            if ranking_foreign <= B:
                passed_num += 1
                ranking_foreign += 1
                results.append('Yes')
            else:
                results.append('No')
        elif examinee == 'c':
            results.append('No')
    else:
        results.append('No')

for result in results:
    print(result)
