


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


def quickSort(arr: list[int], order="asc"):
    assert order == "asc" or order == "desc", "The order can only be 'asc' or 'desc'."
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) - 1]
    left = []
    right = []
    for i in range(len(arr)-1):
        if order == "desc":
            if arr[i] > pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        else:
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
    return quickSort(left, order) + [pivot] + quickSort(right, order)



print(f"Unsorted elements: {elements}")
asc = quickSort(elements)
print(f"Sorted Asc: elements: {asc}")
desc = quickSort(elements, 'desc')
print(f"Sorted Desc: elements: {desc}")