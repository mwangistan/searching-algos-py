def lsearch(lst, elem):
    '''Linearly search for an item (elem) in a list return True if found
    '''
    if len(lst) == 0:
        return False

    for i in lst:
        if i == elem:
            return True
    return False
