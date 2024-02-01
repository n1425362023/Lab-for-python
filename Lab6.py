# Q2: Insert Items
def insert_items(s, before, after):
    lst = s.copy()
    num = 1
    for i in range(len(lst)):
        if lst[i] == before:
            s.insert(i + num, after)
            num += 1
    return s


# Q4: Count Occurrences
def count_occurrences(t, n, x):
    num = 0
    for i in range(n):
        if (next(t) ==
                x):
            num += 1
    return num


# Q5: Repeated
def repeated(t, k):
    num = 0
    target = next(t)
    for i in t:
        if i == target:
            num += 1
            if num == k:
                return i
        else:
            num = 1
            target = i
    return None


# Q6: Partial Reverse
def partial_reverse(s, start):
    s[start:] = s[start:][::-1]
    return s
