from lab05 import *
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

## Extra Rooted Trees, Linked Lists, Dictionaries Questions ##

################
# Rooted Trees #
################

# Q5
def height(t):
    """Return the depth of the deepest node in the tree. 

    >>> height(leaf(1))
    0
    >>> height(rooted(1, [leaf(2), leaf(3)]))
    1
    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    >>> height(t)
    2
    """
    "*** YOUR CODE HERE ***"

################
# Linked Lists #
################

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        if is_link(first(lst)):
            s = s + linked_list_to_str(first(lst)) + ' '
        else:
            s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s + '>'

def print_linked_list(lst):
    """
    >>> print_linked_list(empty)
    < >
    >>> print_linked_list(link(1, empty))
    < 1 >
    >>> print_linked_list(link(2, link(3, link(link(4, empty), empty))))
    < 2 3 < 4 > >
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), \
            link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))

# Q6
def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """

#lst1 = link(1, link(2, link(3, empty)))
#print(link_to_list(lst1))
# Q7
def insert_at_end(lst, elem):
    """Return a linked list that is the same as lst with elem added
    at the end.

    >>> lst1 = insert_at_end(empty, 1)
    >>> print_linked_list(lst1)
    < 1 >
    >>> lst2 = insert_at_end(lst1, 2)
    >>> print_linked_list(lst2)
    < 1 2 >
    >>> lst3 = insert_at_end(lst2, 3)
    >>> print_linked_list(lst3)
    < 1 2 3 >
    """
    new_list = []
    if lst == empty:
        new_list = [elem,lst]
    else:
        a = link(first(lst))
        b = link(a.append(rest(elem)))
        c = link(a,b)
        return c

lst1 = insert_at_end(empty, 1)

lst2 = insert_at_end(lst1, 2)

lst3 = insert_at_end(lst2, 3)
print (lst3)
################
# Dictionaries #
################

# Q8
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            "*** YOUR CODE HERE ***"
        "*** YOUR CODE HERE ***"
        prev = word
    return table

# Q9
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
    return result + word

# Warning: do NOT try to print the return result of this function
def shakespeare_tokens(path='shakespeare.txt', url='http://goo.gl/SztLfX'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)
