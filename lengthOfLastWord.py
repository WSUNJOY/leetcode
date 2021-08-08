# encoding: utf-8
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: lengthOfLastWord.py
@time: 2019/11/28 11:27 上午
@description:
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
示例:
输入: "Hello World"
输出: 5
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    __slots__ = ('name', 'age')

    @property
    def name(self):
        return self.name

    @name.setter
    def __set_name__(self, owner, name):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif " " in s:
            return len(s.rstrip().split(" ")[-1])
        else:
            return len(s)

if __name__ == '__main__':
    s = 'hello world'
    so = Solution()
    so.name = '11'
    print(so.name)
    # print(so.lengthOfLastWord(s))
