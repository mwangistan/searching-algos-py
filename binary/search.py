def bsearch(lst, elem):
    '''Binary search using iteration
    '''
    if len(lst) == 0:
        return False
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = start + (end - start) // 2
        if lst[mid] == elem:
            return True
        elif lst[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1 
    return False

def bsearch_rec(lst, elem, start, end):
    '''Binary search using recursion
    '''
    if len(lst) == 0:
        return False
    if start < end:
        mid = start + (end - start) // 2
        if lst[mid] == elem:
            return True
        elif lst[mid] < elem:
            return bsearch_rec(lst, elem, mid + 1, end)
        else:
            return bsearch_rec(lst, elem, start, mid - 1 )
         