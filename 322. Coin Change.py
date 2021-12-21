"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
你可以认为每种硬币的数量是无限的。

示例1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import sys
from typing import List


class Solution:
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        n = len(coins)

        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                if dp[j] - 1 > dp[j - coins[i - 1]]:
                    dp[j] = 1 + dp[j - coins[i - 1]]
        if dp[amount] == sys.maxsize:
            return -1
        else:
            return dp[amount]
