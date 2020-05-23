""" Module solution """
from typing import List


class Solution:
    """ Challenge solution """

    def duplicate_zeros(self, arr: List[int]):
        """Duplicate zeros and shift right"""
        index = 0
        for step, value in enumerate(arr):
            if value == 0 and step >= index:
                arr[step + 1:] = arr[step:-1]
                index = step + 2
