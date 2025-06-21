#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    answer = N if not N % 2 else N * 2
    print(answer)

if __name__ == '__main__':
    main()
