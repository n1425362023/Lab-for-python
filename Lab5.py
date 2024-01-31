import math


class tree:
    def __init__(self, value, branches=None):
        self.value = value
        self.branches = branches if branches is not None else []


class make_city:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class lat_lon:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Q2: Finding Berries!
def berry_finder(t):
    if t.value == 'berry':
        return True
    for branch in t.branches:
        if berry_finder(branch):
            return True
    return False


# Q3: Replace Loki at Leaf
def replace_loki_at_leaf(t, lokis_replacement):
    if t.value == 'loki':
        t.value = 'lokis_replacement'
        return t
    for branch in t.branches:
        replace_loki_at_leaf(branch, lokis_replacement)


# Q4: Distance
def distance(city_a, city_b):
    return math.sqrt((city_b.x - city_a.x) ** 2 + (city_b.y - city_a.y) ** 2)


# Q5: Closer City
def closer_city(lat, lon, city_a, city_b):
    if distance(lat_lon(lat, lon), city_a) < distance(lat_lon(lat, lon), city_b):
        return city_a.name
    else:
        return city_b.name


# Q7: Recursion on Trees:
num = 0


def dejavu(t, n):
    if t.value == n:
        state = True
        return state
    else:
        state = False
    if t.branches is not None:
        for branch in t.branches:
            if dejavu(branch, n-t.value):
                return True
    return state
