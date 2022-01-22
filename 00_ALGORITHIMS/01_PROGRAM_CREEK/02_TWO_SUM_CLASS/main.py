class TwoSum:
    """
    Stores numbers with their count in the elements hash map.
    When using find each element used to find the target.
    Check if the target is within the hash map.
    If it is, and the target is the same as the current element,
    i.e. n = 14, i = 7, target = 7, then make sure more than
    one of that element exists in the hash map.
    """

    def __init__(self):
        self.elements = {}  # k = number, v = count

    def add(self, n: int) -> None:
        if n in self.elements.keys():
            self.elements[n] += 1
        else:
            self.elements[n] = 1

    # {4:1, 9:1, 6:1, 5:1}
    def find(self, n: int) -> bool:
        for i in self.elements.keys():
            target = n - i # 9 - 4 = 9
            if target in self.elements.keys():
                if i == target and self.elements[target] < 2:
                    continue
                return True
        return False


two_sum = TwoSum()
two_sum.add(4)
two_sum.add(9)
two_sum.add(6)
two_sum.add(5)


assert two_sum.find(14) == True
assert two_sum.find(9) == True
assert two_sum.find(16) == False
assert two_sum.find(4) == False
