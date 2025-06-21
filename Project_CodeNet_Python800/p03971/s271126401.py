def main():
    quantity, A, B = map(int, input().split())
    l = list(input())
    yes = 0
    abroad = 0

    for i in range(quantity):
        if l[i] == 'a':
            if yes < (A + B):
                print('Yes')
                yes = yes + 1
            else:
                print('No')
        
        if l[i] == 'b':
            abroad = abroad + 1
            if yes < (A + B) and abroad <= B:
                print('Yes')
                yes = yes + 1

            else:
                print('No')
        
        if l[i] == 'c':
            print('No')

main()