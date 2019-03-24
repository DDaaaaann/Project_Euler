# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

_range = range(1, 1000)
equals = 1000


def is_pythagorean_triplet(_a, _b, _c):
    return _a**2 + _b**2 == _c**2


def product(_a, _b, _c):
    return _a * _b * _c


def run():
    for a in _range:
        for b in _range:
            c = equals - a - b
            if is_pythagorean_triplet(a, b, c):
                return product(a, b, c)


print run()
