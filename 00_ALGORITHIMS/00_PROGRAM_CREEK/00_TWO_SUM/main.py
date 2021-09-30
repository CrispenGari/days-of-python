from typing import Tuple
def two_sum(numbers: list, target: int) -> Tuple[int, int]:
    """
    The hash map `keys` become the value needed for the int at the index given by the
    has map `value` to equal the result. So all you need to do is for each number check
    if it exists in these "needed" numbers.
    """
    if not numbers:
        return None

    hash_map = {}

    # [2, 7, 11, 15], 26
    for i, n in enumerate(numbers):
        if n in hash_map.keys():
            print(f"{i}, {n}")
            idx = hash_map[n] # 0
            index1 = idx # 0
            index2 = i # 1
            return index1, index2
        else:
            hash_map[target - n] = i
    return None


assert two_sum([2, 7, 11, 15], 9) == (0, 1), "condition 1 failed"
assert two_sum([2, 7, 11, 15], 26) == (2, 3), "condition 2 failed"
assert two_sum([2, 7, 11, 16], 26) == None, "condition 3 failed"
assert two_sum([], 26) == None, "condition 4 failed"