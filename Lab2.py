# Q4: Composite Identity Function
def composer(f, g):
    return lambda x: f(g(x))


add_one = lambda x: x + 1
square = lambda x: x ** 2

compose = composer(square, add_one)
print(compose(5))


def composite_identify(f, g):
    return lambda x: f(g(x)) == g(f(x))


print(composite_identify(add_one, square)(5))


# Q5: Count van Count
def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def sum_digits(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total


def count_cond(condition):
    return lambda n, *i: condition(n, i)


# Q7: Multiple
def multiple(a, b):
    num = a * b
    while b:
        tmp = b
        b = a % b
        a = tmp
    return num // tmp


print(multiple(3, 4))


# Q8: I Heard You Liked Functions...
def cycle(f1, f2, f3):
    def mode(n):
        def f(x):
            num = x
            i = 1
            while i <= n:
                if i == 1:
                    num = f1(num)
                    i += 1
                    continue
                elif i == 2:
                    num = f2(num)
                    i += 1
                    continue
                elif i == 3:
                    num = f3(num)
                    i += 1
                    continue
                else:
                    i -= 3
            return num

        return f

    return mode


def add1(x):
    return x + 1


def times2(x):
    return x * 2


def add3(x):
    return x + 3


my_cycle = cycle(add1, times2, add3)
identity = my_cycle(2)
print(identity(1))
