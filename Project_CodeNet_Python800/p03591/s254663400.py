#! /bin/python
# coding:utf-8

import re
import itertools

S = raw_input()
matchOBJ = re.search(r'^YAKI', S)

if (matchOBJ):
    print "Yes"
else:
    print "No"
