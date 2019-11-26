# encoding: utf-8
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: maxSubArray.py
@time: 2019/11/26 10:52 下午
"""
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        max_sum = 0
        for i in range(len(nums)):
            if max_sum > 0:
                max_sum += nums[i]
            else:
                max_sum = nums[i]
            res = max(res,max_sum)
        return res
if __name__ == '__main__':
    nums = [2, -7, 11, 15]
    so = Solution()
    print(so.maxSubArray(nums))