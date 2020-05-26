""" Module solution """
from typing import List


class Solution:
    """ Challenge solution """

    def duplicate_zeros(self, arr: List[int]):
        """Duplicate zeros and shift right"""
        length = len(arr)
        zeros = []
        for step, value in enumerate(arr):
            if value == 0:
                zeros.append(step)

        length_zeros = len(zeros)
        if length_zeros > 0 and length_zeros < length:
            for step, value in enumerate(zeros):
                arr[value + step + 1:] = arr[value + step:-1]
                