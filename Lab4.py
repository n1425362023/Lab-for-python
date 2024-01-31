# Q2: Map
def my_map(fn, seq):
    return (fn(x) for x in seq)


# Q3: Filter
def my_filter(pred, seq):
    return (x for x in seq if pred(x))


# Q4: Reduce
def my_reduce(combiner, seq):
    it = iter(seq)
    res = next(it)
    for elem in it:
        res = combiner(res, elem)
    return res


# Q5: Double Eights
def double_eights(n):
    if n < 10:
        return False
    if n % 100 == 88:
        return True
    else:
        return double_eights(n // 10)


# Q6: Merge
def merge(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    elif lst1[0] <= lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    elif lst1[0] > lst2[0]:
        return [lst2[0]] + merge(lst1, lst2[1:])


# Q7: Summation
def summation(n, term):
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n - 1, term)


# Q8: Count Palindromes
def count_palindromes(L):
    lowercase_list = list(map(lambda item: item.lower(), L))
    lst = filter(lambda item: item == item[::-1], lowercase_list)
    return len(list(lst))
