# encoding: utf-8
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: isValid.py
@time: 2019/10/29 7:00 下午
"""

class Solution(object):
    def isValid(self, s):
        """
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
        有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。
        示例 1:
        输入: "()"
        输出: true
        示例 2:
        输入: "()[]{}"
        输出: true
        示例 3:
        输入: "(]"
        输出: false
        示例 4:
        输入: "([)]"
        输出: false
        示例 5:
        输入: "{[]}"
        输出: true
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/valid-parentheses
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == '__main__':
    s = "]["
    so = Solution()
    print(so.isValid(s))