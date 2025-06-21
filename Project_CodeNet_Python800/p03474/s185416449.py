import re
n,m=input().split();print('YNeos'[not re.match(r'[0-9]{'+n+'}-[0-9]{'+m+'}',input())::2])