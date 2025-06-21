S = input()
counter = 0
for i in range(1, len(S)):
    previous_color = S[i - 1]
    checking_color = S[i]
    if previous_color == checking_color:
        counter += 1
        if previous_color == '0':
            S = S[:i] + '1' + S[i + 1:]
        else:
            S = S[:i] + '0' + S[i + 1:]
print(min(counter, abs(len(S) - counter)))
