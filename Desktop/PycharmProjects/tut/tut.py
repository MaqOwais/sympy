m = list(str(input()))
n = []
o = []
r = []
u = []
v = []
for l in set(m):
    w = [l, m.count(l)]
    w.reverse()
    n.append(w[0])
    o.append(w)

for l in set(m):
    w = [l, m.count(l)]
    v.append(w)
z = sorted(v)
p = sorted(set(n), reverse=True)
tr = [tuple(io) for io in z]
AZ = sorted(sorted(tr, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
q = [list(elem) for elem in AZ]
for ie in q:
    lep = ie[0]
    ie[0] = ie[1]
    ie[1] = lep
for i in range(3):
    r.append(q[i][1])
for x in range(3):
    u.append(q[x][0])
for c, v in zip(r, u):
    print(c, v)
print("  ")
print("the total no of elements in the input given is : " , sum(u))