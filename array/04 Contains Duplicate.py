"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    @staticmethod
    def is_contain_duplicate(nums:list[int]) -> bool:
        from collections import Counter
        distinct = any([value for value in Counter(nums).values() if value > 1])
        return distinct


if __name__ == "__main__":
    sol = Solution()
    # Input: nums = [1,2,3,1]
    # Output: true
    assert sol.is_contain_duplicate([1, 2, 3, 1])
    # Input: nums = [1,2,3,4]
    # Output: false
    assert not sol.is_contain_duplicate([1, 2, 3, 4, 5])
    # Input: nums = [1,1,1,3,3,4,3,2,4,2]
    # Output: true
    assert sol.is_contain_duplicate([1, 2, 3,3, 4, 3, 2, 4, 2, 1, 1, 1, 1])
    print("All Test Cases Passed")