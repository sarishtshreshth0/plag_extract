#!/usr/bin/env python3
import re
a, b, s = open(0).read().split()
r = "^\d{" + a + "}-\d{" + b + "}$"
print("YNeos"[re.findall(r, s) == []::2])
