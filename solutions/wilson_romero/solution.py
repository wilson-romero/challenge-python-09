""" Module solution """
from typing import List

class Solution:
    """ Challenge solution """
    def duplicate_zeros(self, arr: List[int]):
        """ Modify the list by doubling the zeros and correcting the items to the right. """ 
        next_index = 0
        length = len(arr)
        while True:
            try:
                next_index = arr.index(0, next_index)
                arr.insert(next_index + 1, 0)
                arr.pop()
                next_index = next_index + 2
            except ValueError:
                break
        arr = arr[:length]
