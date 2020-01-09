import math

def jsearch(lst, elem):
    if len(lst) == 0:
        return False
    n = len(lst)
    step = math.sqrt(n)
    prev = 0
    while lst[int(min(step, n)-1)] < elem:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return False
    
    # Linear search for elem in lst beginning with prev
    while lst[prev] < elem:
        prev += 1

        # If we've reached the end of the array elem is not present
        if prev == min(step, n):
            return False
        
    if lst[int(prev)] == elem:
        return True
    return False