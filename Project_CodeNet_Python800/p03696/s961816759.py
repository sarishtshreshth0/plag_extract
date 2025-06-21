N = 6
S = ')))())'


# N = 8
# S = '))))(((('

# N = 3
# S = '())'

# N = 9
# S = '(())()()('

N = int(input())
S = input()

def calculate(n, str):

    finalStr = ''
    while True:
        point = 0
        remainStr = ''
        for i in range(len(str)):
            if i > 0:
                if (str[i-1] == '(') and (str[i] == ')'):
                    point += 1
                    continue

            if i < (n - 1):
                if (str[i] == '(') and (str[i+1] == ')'):
                    point += 1
                    continue

            remainStr += str[i]

        str = remainStr
        n = len(str)
        if point == 0:
            finalStr = remainStr
            return finalStr
            break







res = calculate(N, S)

for i in range(len(res)):
    if res[i] == '(':
        S = S + ')'

    if res[i] == ')':
        S = '(' + S

print(S)
# print(result)
