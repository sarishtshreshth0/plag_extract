import re
n,m=input().split();print('YNeos'[re.match(r'[0-9]{'+n+'}-[0-9]{'+m+'}',input()) is None::2])