from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            x = nums[m]
            if x == target:
                return True
            if x == nums[l]:
                l += 1  # 去重重复值情况
            elif nums[l] < x:  # 前半部分有序
                if nums[l] <= target <= x:  # 目标值在前半部分
                    r = m - 1
                else:  # 反之，去后半部分找
                    l = m + 1
            else:  # 后半部分有序
                if x <= target <= nums[r]:  # 目标值在后半部分
                    l = m + 1
                else:  # 反之，去前半部分找
                    r = m - 1
        return False  # 没找到值
