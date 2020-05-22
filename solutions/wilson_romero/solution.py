from typing import List


class Solution:

    def duplicate_zeros(self, arr: List[int]):
        # AQUÍ VA TU SOLUCIÓN
        indices = list(filter(lambda x: arr[x] == 0, range(len(arr))))
        shift = 0
        for i in indices:
            arr.insert(i + shift, 0)
            arr.pop()
            shift = shift + 1
