n = input()
fn = sum(int(i) for i in n)
print('Yes' if int(n) % fn == 0 else 'No')