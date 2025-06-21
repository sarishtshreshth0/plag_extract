import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('a1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    s = read_str()
    if s[0:4] == 'YAKI':
        print('Yes')
    else:
        print('No')


main()
