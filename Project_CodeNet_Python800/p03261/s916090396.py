def f(words):
	seen = set([words[0]])
	p = words[0]
	for w in words[1:]:
		if w in seen or p[-1] != w[0]: return False
		p = w
		seen.add(w)
	return True

print 'Yes' if f([raw_input() for _ in range(int(raw_input()))]) else 'No'
