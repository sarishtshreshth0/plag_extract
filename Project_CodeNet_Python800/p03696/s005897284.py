input()
t=s=input()
while"()"in s:s=s.replace("()","")
print("("*s.count(")")+t+")"*s.count("("))