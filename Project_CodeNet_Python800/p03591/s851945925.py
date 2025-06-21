def func() :
    s=input()
    if len(s) >= len('YAKI') :
        if s[:4] == 'YAKI' :
            print('Yes')
            return
    print('No')
func()