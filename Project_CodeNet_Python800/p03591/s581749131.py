def main():
    S = input()

    try:
        if S.index('YAKI'):
            ans = 'No'
        else:
            ans = 'Yes'
    except:
        ans = 'No'

    print(ans)

main()
