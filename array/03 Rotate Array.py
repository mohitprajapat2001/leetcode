"""
Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution:

    @staticmethod
    def rotate_array(nums: list[int] ,k=int) -> list[int]:
        k = k%len(nums)
        return nums[-k:] + nums[:-k]

if __name__ == "__main__":
    sol = Solution()

    # Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    # Output: [5, 6, 7, 1, 2, 3, 4]
    assert  [5, 6, 7, 1, 2, 3, 4] == sol.rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
    # Input: nums = [-1,-100,3,99], k = 2
    # Output: [3,99,-1,-100]
    assert [3,99,-1,-100] == sol.rotate_array([-1,-100,3,99], 2)
    print("ALl Test Cases Passed")