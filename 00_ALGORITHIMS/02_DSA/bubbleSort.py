
elements = [3, -1, 8, 8, 7, 1, 10, -6]
def bubbleSort(elements, order="asc"):
    assert order == "asc" or order == "desc", "The order can only be 'asc' or 'desc'."
    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(elements) - 1):
            if order == 'desc':
                if elements[idx] < elements[idx + 1]:
                    elements[idx], elements[idx + 1] = elements[idx + 1], elements[idx]
                    swapped = True
            else:
                if elements[idx] > elements[idx + 1]:
                    elements[idx], elements[idx + 1] = elements[idx + 1], elements[idx]
                    swapped = True

# O(n^2)
print(f"Unsorted elements: {elements}")
bubbleSort(elements, "asc")
print(f"Sorted Asc: elements: {elements}")
bubbleSort(elements, "desc")
print(f"Sorted Desc: elements: {elements}")