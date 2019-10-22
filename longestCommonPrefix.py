# encoding: utf-8
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: longestCommonPrefix.py
@time: 2019/10/21 7:18 下午
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        编写一个函数来查找字符串数组中的最长公共前缀。
        如果不存在公共前缀，返回空字符串 ""。
        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"
        示例 2:

        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。
        说明:所有输入只包含小写字母 a-z 。
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/longest-common-prefix
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :param strs:
        :return:
        """
        if len(strs) == 0:
            return ""
        res = ''
        for c in zip(*strs):
            print(zip(*strs))
            if len(set(c)) == 1:
                res += c[0]
            else:
                break
        return res

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    # strs = []
    so = Solution()
    print(so.longestCommonPrefix(strs))