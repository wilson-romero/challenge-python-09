
from typing import List


def duplicate_zeros(arr: List[int]):
    # AQUÍ VA TU SOLUCIÓN
    index = 0
    start = 0
    for step, value in enumerate(arr):
        if value == 0 and step >= index:
            print(step, value, index)
            arr[step + 1:] = arr[step:-1]
            index = step + 2


if __name__ == "__main__":
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr)
    print(arr)
