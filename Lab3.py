# Q1: Ordered Digits
import math


def ordered_digits(x):
    return "".join(sorted(str(x))) == str(x)


# Q2: K Runner
def get_k_run_starter(n, k):
    i = 0
    final = None
    while i <= k:
        while n % 10 > n // 10 % 10:
            n = n // 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


# Q3: Nearest Power of Two
def nearest_two(x):
    return 2 ** round(math.log(x, 2))


# Q4: Make Repeater
def make_repeater(func, n):
    def fun(x):
        for i in range(n):
            x = func(x)
        return x

    return fun


# Q5: Apply Twice
def apply_twice(func):
    return lambda x: func(func(x))


# Q6: It's Always a Good Prime
def div_by_primes_under(n):
    checker = lambda x: False
    i = 2
    while i < n:
        if not checker(i):
            checker = checker = (lambda f, i: lambda x: x % i == 0)(checker, i)
        i = i + 1
    return checker
def div_by_primes_under_no_lambda(n):
    def checker(x):
        return False

    i = 2
    while i <= n:
        if not checker(i):
            def outer():
                def inner(x):
                    return x % i == 0

                return inner

            checker = outer
        i = i + 1
    return checker
