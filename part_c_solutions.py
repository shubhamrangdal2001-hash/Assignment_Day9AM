# part_c_solutions.py
# Part C: Interview Ready - Coding and Debug Solutions

import copy


# -------------------------------------------------------
# Q1 - Shallow Copy vs Deep Copy (demonstrated in code)
# -------------------------------------------------------
def demo_copy():
    print("=" * 50)
    print("Q1 - Shallow Copy vs Deep Copy Demo")
    print("=" * 50)

    original = [[1, 2, 3], [4, 5, 6]]

    # Shallow copy - copies the outer list, inner lists are still shared
    shallow = copy.copy(original)
    shallow[0][0] = 99  # this changes original too!

    print(f"\nAfter shallow copy and modifying shallow[0][0] = 99:")
    print(f"  Original: {original}")   # shows 99 - affected!
    print(f"  Shallow:  {shallow}")

    # Deep copy - fully independent copy at all levels
    original2 = [[1, 2, 3], [4, 5, 6]]
    deep = copy.deepcopy(original2)
    deep[0][0] = 99  # original2 is NOT affected

    print(f"\nAfter deep copy and modifying deep[0][0] = 99:")
    print(f"  Original2: {original2}")  # still [1, 2, 3]
    print(f"  Deep:      {deep}")


# -------------------------------------------------------
# Q2 - List Rotation
# -------------------------------------------------------
def rotate_list(lst, k):
    """
    Rotates list to the right by k positions.
    Handles k > len(lst) using modulo.
    Example: rotate_list([1,2,3,4,5], 2) -> [4,5,1,2,3]
    """
    if not lst:
        return lst
    n = len(lst)
    k = k % n  # handle cases where k > len(lst)
    # Use slicing: last k elements + first n-k elements
    return lst[-k:] + lst[:-k]


# -------------------------------------------------------
# Q3 - Debug Problem
# -------------------------------------------------------
def buggy_version():
    """
    This version has the bug - modifying list while iterating.
    It accidentally skips elements because indices shift after each removal.
    Try [2,4,6,8] to clearly see the bug.
    """
    nums = [2, 4, 6, 8]  # using all-even list to show the bug clearly
    for num in nums:
        if num % 2 == 0:
            nums.remove(num)
    return nums  # Expected: [] but gets [4, 8]


def fixed_version():
    """Correct version using list comprehension."""
    nums = [2, 4, 6, 8]
    nums = [num for num in nums if num % 2 != 0]
    return nums  # Correctly returns []


def fixed_version_original():
    """Fixed for original list [1..8] -> [1,3,5,7]"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums = [num for num in nums if num % 2 != 0]
    return nums


# -------------------------------------------------------
# Running all demos
# -------------------------------------------------------
if __name__ == "__main__":

    # Q1 Demo
    demo_copy()

    # Q2 Demo
    print("\n" + "=" * 50)
    print("Q2 - List Rotation")
    print("=" * 50)
    print(f"\n  rotate_list([1,2,3,4,5], 2)  -> {rotate_list([1, 2, 3, 4, 5], 2)}")
    print(f"  rotate_list([1,2,3,4,5], 7)  -> {rotate_list([1, 2, 3, 4, 5], 7)}")
    print(f"  rotate_list([1,2,3,4,5], 0)  -> {rotate_list([1, 2, 3, 4, 5], 0)}")
    print(f"  rotate_list([1,2,3,4,5], 5)  -> {rotate_list([1, 2, 3, 4, 5], 5)}")

    # Q3 Demo
    print("\n" + "=" * 50)
    print("Q3 - Debug Problem")
    print("=" * 50)
    print(f"\n  Buggy output  [2,4,6,8]: {buggy_version()}")      # [4, 8] - wrong!
    print(f"  Fixed output  [2,4,6,8]: {fixed_version()}")        # [] - correct
    print(f"  Fixed [1..8] output    : {fixed_version_original()}")  # [1,3,5,7]
