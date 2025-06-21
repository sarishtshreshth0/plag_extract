S = input()
fn = sum(map(int, S))
print('Yes' if int(S)%fn == 0 else 'No')