#
# abc070 b
#
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """0 75 25 100"""
        output = """50"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 33 66 99"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 90 20 80"""
        output = """60"""
        self.assertIO(input, output)


def resolve():
    A, B, C, D = map(int, input().split())

    if A > C:
        A, C = C, A
        B, D = D, B

    if B < D:
        print(max(0, B-C))
    else:
        print(D-C)


if __name__ == "__main__":
    # unittest.main()
    resolve()
