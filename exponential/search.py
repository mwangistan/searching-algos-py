def esearch(lst, elem):
    n = len(lst)
    if n == 0:
        return 0
    for i in range(0, n):
        step = i ** 2
        return bsearch(lst, elem, step//2, min(step, n))

def bsearch(lst, elem, start, end):
    if start<=end:
        mid = start + (end - start) // 2
        if lst[mid] == elem:
            return True
        elif lst[mid] > elem:
            return bsearch(lst, elem, start, mid - 1)
        else:
            return bsearch(lst, elem, mid + 1, end)