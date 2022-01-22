
def linear_search(elements:list, target:int)->int:
    for index in range(0, len(elements)):
        if elements[index] == target:
            """
            if the element if found we return the index of the element
            """
            return index
    """
    If the element is not found we return a nagative index
    """ 
    return -1
    
# Testing the algorithim
numbers = [i for i in range(10)]

assert linear_search(numbers, 6) == 6, "The element was not found."
assert linear_search(numbers, 10) == -1, "The element was not found"