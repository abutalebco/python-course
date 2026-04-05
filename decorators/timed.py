import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!")
        return value
    
    return wrapper

@timed
def quick_sort(array):
    def _quick_sort(arr):
        if len(arr) < 2:
            return arr
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return _quick_sort(less) + [pivot] + _quick_sort(greater)

    return _quick_sort(array)

quick_sort([9, 34, 56, 7, 8, 3, 44])