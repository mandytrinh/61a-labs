## Extra Linked List Class and Generic Functions ##

######################
# Linked Lists Class #
######################

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __add__(self, other):
        """Adds two Links, returning a new Link

        >>> Link(1, Link(2)) + Link(3, Link(4, Link(5)))
        Link(1, Link(2, Link(3, Link(4, Link(5)))))
        """
        "*** YOUR CODE HERE ***"

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        "*** YOUR CODE HERE ***"

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> rlist_to_list(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    lst = []
    while link is not Link.empty:
        lst.append(link.first)
        link = link.rest
    return lst

#link = Link(1, Link(2, Link(3, Link(4))))
#print(link_to_list(link))
#[1, 2, 3, 4]
#print(rlist_to_list(Link.empty))
#[]

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> Link(1).rest is Link.empty
    True
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> reverse(Link(1))
    Link(1)
    """
    if link is Link.empty:
        return "this linked list is empty"
    link = Link(link.rest, link.first)
    while link is not Link.empty:
        link.rest = Link(link.rest, link.first)
        link = link.rest
    return Link


print(Link(1).rest is Link.empty)
#True
link = Link(1, Link(2, Link(3)))
print(reverse(link))
#Link(3, Link(2, Link(1)))
print(reverse(Link(1)))
#Link(1)


def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {
    list : 'list',
    Link : 'link'
}

def concat(seq1, seq2):
    """Takes the elements of seq1 and seq2 and adds them together.

    >>> link = Link(4, Link(5, Link(6)))
    >>> lst = [1, 2, 3]
    >>> concat(lst, link)
    [1, 2, 3, 4, 5, 6]
    >>> concat(link, [7, 8])
    Link(4, Link(5, Link(6, Link(7, Link(8)))))
    >>> concat(lst, [7, 8, 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if type_tag(seq1) == type_tag(seq2):
        return seq1 + seq2
    else:
        types = (type_tag(seq1), type_tag(seq2))
        if types in concat.adders:
            return concat.adders[types](seq1, seq2)

def add_list_link(lst, link):
    "*** YOUR CODE HERE ***"

def add_link_list(link, lst):
    "*** YOUR CODE HERE ***"

concat.adders = {
    ('list', 'link')  : add_list_link,
    ('link', 'list')  : add_link_list
}

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(______, ______, ______)

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
    return foldr(link, step, identity)(z)

