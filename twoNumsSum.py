class Solution(object):
    def twoSum(self, nums, target):
        """
        给定一个整数数组
        nums 和一个目标值
        target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
        示例:
        给定nums = [2, 7, 11, 15], target = 9
        因为nums[0] + nums[1] = 2 + 7 = 9
        所以返回[0, 1]
        来源：力扣（LeetCode）
        链接：https: // leetcode - cn.com / problems / two - sum
        :param nums:
        :param target:
        :return:
        """
        # hashmap = {}
        # for ind, num in enumerate(nums):
        #     hashmap[num] = ind
        # for i, num in enumerate(nums):
        #     j = hashmap.get(target - num)
        #     if j is not None and i != j:
        #         return [i, j]

        len_nums = len(nums)
        if len_nums == 0:
            return []
        for i in range(len_nums):
            if target-nums[i] in nums:
                if nums.count(nums[i]) == 1 and target-nums[i] == nums[i]:
                    continue
                else:
                    return i,nums.index(target-nums[i], i+1)


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    so = Solution()
    print(so.twoSum(nums, target))
