from typing import Tuple


def three_sum_zero(numbers: list) -> list:
    """
    Use two pointers method.
    Take advantage of sorted arrays to help avoid duplicates.
    """
    result = []
    if not numbers or len(numbers) < 3:
        return result
    numbers = sorted(numbers)

    for i in range(len(numbers) - 2):
        # always does on first loop, subsequent loops only if number has actually increased
        # i.e. if list starts with something like [-1, -1, -1, ...], don't need to check all of them
        if i == 0 or numbers[i] > numbers[i - 1]:
            j = i + 1  # pointing to "start" of list, but ahead of number[i]
            k = len(numbers) - 1  # pointing at "end" of list

            while j < k:  # until the pointers meet, do this while

                x = numbers[i] + numbers[j] + numbers[k]

                if x == 0:  # if the sum is equal to zero, found a three sum!

                    result.append([numbers[i], numbers[j], numbers[k]])

                    j += 1  # move the pointers
                    k -= 1

                    # keep increasing the value of the "start" and "end" pointers
                    # until the values at them actually change
                    while j < k and numbers[j] == numbers[j - 1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k + 1]:
                        k -= 1

                # if the sum of the values are less than zero, increase the "start" pointer
                elif x < 0:
                    j += 1

                # if the sum of the values are greater than zero, deccrease the "end" pointer
                else:
                    k -= 1
    return result

S = [-1, 0, 1, 2, -1, 4]

assert three_sum_zero(S) == [[-1, -1, 2], [-1, 0, 1]]