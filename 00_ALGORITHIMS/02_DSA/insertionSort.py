

elements = [3, -1, 8, 8, 7, 1, 10, -6]
def insertionSort(arr: list[int], order="asc"):
    assert order == "asc" or order == "desc", "The order can only be 'asc' or 'desc'."
    for i in range(1, len(arr)):
        nti = arr[i]
        j = i -1
        if order == 'asc':
            while j >= 0 and arr[j] > nti:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] < nti:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = nti

print(f"Unsorted elements: {elements}")
insertionSort(elements)
print(f"Sorted Asc: elements: {elements}")
insertionSort(elements, "desc")
print(f"Sorted Desc: elements: {elements}")