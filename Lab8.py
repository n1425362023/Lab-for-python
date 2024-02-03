class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def test_empty(link):
        if link is Link.empty:
            print('This linked list is empty!')
        else:
            print('This linked list is not empty!')


# Q2: Duplicate Link
def duplicate_link(link, val):
    if link is Link.empty:
        return
    if link.first == val:
        link.rest = Link(val, link.rest)
        duplicate_link(link.rest.rest, val)
    else:
        duplicate_link(link.rest, val)


# Q3: Convert Link
def convert_link(link):
    if link is Link.empty:
        return []
    else:
        return [link.first] + convert_link(link.rest)


# Q4: Multiply Links
def multiply_lnks(lst_of_lnks):
    product = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return link
        product *= link.first
    lst_of_lnks_rests = [link.rest for link in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))
