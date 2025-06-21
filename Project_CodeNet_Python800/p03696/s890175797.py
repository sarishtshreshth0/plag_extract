n = int(input())
s = str(input())
ns = s
while '()' in ns:
    ns = ns.replace('()', '')
l = ns.count(')')
r = ns.count('(')
print('(' * l + s + ')' * r)