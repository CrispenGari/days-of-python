
def binary_search(elements:list, target:int, start:int =0, end=None)->int:
    if end is None:
        end = len(elements) -1
    if start > end:return -1
    mid = (start + end)//2
    
    if elements[mid] == target:
        return mid
    elif elements[mid] < target:
        return binary_search(elements, target, mid+1, end)
    else:
        return binary_search(elements, target, start, mid-1)
        
# Testing the Algorithm
numbers = [i for i in range(10)]

assert binary_search(numbers, 6) == 6, "The element was not found."
assert binary_search(numbers, 10) == -1, "The element was not found"