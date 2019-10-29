# encoding: utf-8
"""
@version: 1.0
@author: sunjoy
@software: PyCharm
@file: reverse.py
@time: 2019/10/22 7:09 下午
"""
class Solution(object):
    def reverse(self, x):
        """给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
        示例 1:
        输入: 123
        输出: 321
        示例 2:
        输入: -123
        输出: -321
        示例 3:
        输入: 120
        输出: 21
        注意:
        假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
        请根据这个假设，如果反转后整数溢出那么就返回 0。
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/reverse-integer
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

        # error method
        # 2 ^ 31 - 1 = 2147483647, -2 ^ 31 = -2147483648
        # if x == 0 or x <= -2147483648 or x >= 2147483647:
        #     return 0
        # absx = abs(x)
        # res = ''
        # while(absx // 10):
        #     res += str(absx % 10)
        #     absx = (absx - absx % 10) // 10
        # res += str(absx)
        # res = res.lstrip('0')
        # if x > 0 and int(res) < 2147483647:
        #     return res
        # elif x < 0 and int(res) > -2147483648:
        #     return '-' + res
        # else:
        #     return 0


        # other's method
        # s = str(x)[::-1].rstrip('-')
        # if int(s) < 2 ** 31:
        #     if x >= 0:
        #         return int(s)
        #     else:
        #         return 0 - int(s)
        # return 0

        s = str(x)[::-1].rstrip('-')
        if int(s) < 2 ** 31:
            if x >= 0:
                return int(s)
            else:
                return 0 - int(s)
        else:
            return 0

if __name__ == '__main__':
    x = -123
    so = Solution()
    print(so.reverse(x))