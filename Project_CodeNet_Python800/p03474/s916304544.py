import re
n=[*input()];print('YNeos'[not re.match(r'[0-9]{'+n[0]+'}-[0-9]{'+n[-1]+'}',input())::2])