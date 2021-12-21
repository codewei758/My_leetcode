from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            temp = nums[i]
            try:
                if nums[i + 1] == temp:
                    i += 2
                    while nums[i] == temp:
                        del nums[i]
                else:
                    i += 1
            except IndexError:
                break

        return len(nums)
