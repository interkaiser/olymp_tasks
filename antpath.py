from math import *
def dist(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return (x ** 2 + y ** 2) ** 0.5
fh = open("INPUT")
f = fh.read().split(" ")
for i in f:
    n = i.split(".")
    a = 0.0
    for d in n[0]:
        a *= 10
        a += ord(d) - 48
    if '.' in i:
        h = 0.1
        for d in n[1]:
            a += h * (ord(d) - 48)
            h /= 10
    f[f.index(i)] = a
p1 = (f[0], f[1])
p2 = (f[2], f[3])
t = (f[4], f[5])
r = f[6]
del(f)
fh.close()
pp = dist(p1, p2)
t1 = dist(p1, t)
t2 = dist(p2, t)
p = (pp + t1 + t2) / 2
s = (p * (p - pp) * (p - t1) * (p - t2)) ** 0.5
del(p)
hit = pp * r > s * 2
if not hit:
    del(s)
    o = open("OUTPUT", "w")
    o.write(str.format("%f" % pp))
    o.close()
else:
    h = 2 * s / pp
    del(s)
    a = acos(h / t1) + acos(h / t2) - acos(r / t1) - acos(r / t2)
    d1 = (t1 ** 2 - r ** 2) ** 0.5
    d2 = (t2 ** 2 - r ** 2) ** 0.5
    d3 = r * a
    del(a)
    o = open("OUTPUT", "w")
    o.write(str.format("%f" % (d1 + d2 + d3)))
    o.close()
