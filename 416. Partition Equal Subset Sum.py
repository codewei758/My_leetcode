from typing import List

"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def canPartition(nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        m = sum(nums) // 2
        n = len(nums)
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(m, nums[i - 1] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i - 1]]

        return dp[m]


nums = [1, 5, 11, 5]
Solution.canPartition(nums=nums)
