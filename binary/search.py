def bsearch(lst, elem):
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