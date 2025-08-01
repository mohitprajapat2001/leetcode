"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit
"""

class Solution:

    @staticmethod
    def best_time_to_buy_sale_stock(nums: list[int])-> int:
        profit = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                profit += nums[i+1] - nums[i]

        return profit

if __name__ == "__main__":
    solution = Solution()
    # [7,1,5,3,6,4] return 7
    assert 7 == solution.best_time_to_buy_sale_stock([7,1,5,3,6,4])
    # [1,2,3,4,5] return 4
    assert 4 == solution.best_time_to_buy_sale_stock([1,2,3,4,5])
    # [7,6,4,3,1] return 0
    assert 0 == solution.best_time_to_buy_sale_stock([7,6,4,3,1])
    print("All Test Cases Passed")