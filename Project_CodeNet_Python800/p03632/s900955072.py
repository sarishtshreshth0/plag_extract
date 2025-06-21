a,b,c,d = map(int,input().split())
figs = [a,b,c,d]
new_figs = sorted(figs)

if b<c or a>d:
    print(0)
    exit()

print(new_figs[2]-new_figs[1])
