from_user=input()
coordinates_str=from_user.split(' ')
A=int(coordinates_str[0])
B=int(coordinates_str[1])
C=int(coordinates_str[2])

if C > A:
    if C < B:
        print('Yes')
    else:
        print('No')

if C < A:
    if C > B:
        print('Yes')
    else:
        print('No')