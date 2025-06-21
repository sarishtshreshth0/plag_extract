def actual(a, b, s):
    if s[a] != '-':
        return 'No'

    for i in range(0, a):
        if not '0' <= s[i] <= '9':
            return 'No'

    for j in range(a + 1, len(s)):
        if not '0' <= s[j] <= '9':
            return 'No'

    return 'Yes'


a, b = map(int, input().split())
s = input()

print(actual(a, b, s))
