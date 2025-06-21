#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input())
fh=x//500
x = x - (500*fh)
f = x//5
print(1000*fh+5*f)