def isYaki(S):
    if len(S) < 4:
        return 'No'
    
    answer = 'YAKI'
    for (a, b) in zip(answer, S):
        if a != b:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    S = input()
    print(isYaki(S))
