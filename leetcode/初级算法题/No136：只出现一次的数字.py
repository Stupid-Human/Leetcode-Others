# 题目说明
'''
[NO.136 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''

# 解法1
'''
	来源于 https://blog.csdn.net/biezhihua/article/details/79571917
	使用异或操作，同0异1，0与任何数进行异或操作的结果是这个数，两个相同的数进行异或操作结果为0。
'''
class Solution(object):
    def __init__(self,nums):
        self.nums = nums
    def singleNumber(self):
        res = 0
        for i in range(len(self.nums)):
            res ^= self.nums[i]
        return res 
# 测试
attri = [2,2,1,23,88,9,23,9,88,121,2323,2323,121,1,12,12,100]
result = Solution(attri)
result.singleNumber()