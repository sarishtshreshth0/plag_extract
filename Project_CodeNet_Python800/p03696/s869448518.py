N = int(input())
S = input()

res = ""
st = []
for s in S:
    if s == "(":
        st.append("(")
        res += "("
    else:
        if st:
            st.pop()
            res += ")"
        else:
            res = "(" + res + ")"

print(res + ")" * len(st))
