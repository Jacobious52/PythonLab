
m = []
for i in xrange(1000):
	if i % 3 == 0 or i % 5 == 0:
		m.append(i)

print sum(m)
