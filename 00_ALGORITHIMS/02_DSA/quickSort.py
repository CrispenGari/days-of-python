
elements = [3, -1, 8, 8, 7, 1, 10, -6]

def quickSortAsc(arr: list[int]):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) - 1]
    left = []
    right = []
    for i in range(len(arr)-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quickSortAsc(left) + [pivot] + quickSortAsc(right)


def quickSortDesc(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) - 1]
    left = []
    right = []
    for i in range(len(arr)-1):
        if arr[i] > pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quickSortDesc(left) + [pivot] + quickSortDesc(right)



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

print(f"Unsorted elements: {elements}")
asc = quickSortAsc(elements)
print(f"Sorted Asc: elements: {asc}")
desc = quickSortDesc(elements)
print(f"Sorted Desc: elements: {desc}")

