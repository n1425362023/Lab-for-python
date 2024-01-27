def falling(n, k):
    num = n
    if 0 < k <= n:
        num = n
        while k > 1:
            n -= 1
            k -= 1
            num *= n
        return num
    elif k == 0:
        num = 1
        return num
    else:
        return False


def divisible_by_k(n, k):
    num = 0
    for i in range(1, n + 1):
        if i % k == 0:
            num += 1
            print(i)
    return num


def sum_digits(y):
    sum = 0
    while y > 0:
        sum += y % 10
        y //= 10
    return sum
