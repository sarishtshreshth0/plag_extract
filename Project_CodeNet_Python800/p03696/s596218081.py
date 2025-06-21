
def resolve():
    N = int(input())
    S = list(input())
    nopen = 0
    addleft = 0
    addright = 0
    for s in S:
        if s == "(":
            nopen += 1
        else:
            if nopen == 0:
                addleft += 1
            else:
                nopen -= 1
    addright = nopen
    print("("*addleft+"".join(S)+")"*addright)


if __name__ == '__main__':
    resolve()