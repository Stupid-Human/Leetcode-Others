'''题目说明：
[NO344 反转字符串](https://leetcode-cn.com/problems/reverse-string)

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
'''

# 解法1
# 前后替换，申请一个变量，前后替换时暂存元素。
class Solution(object):
    def __init__(self,s):
        self.s = s
    def reverseString(self):
        tmp = ''
        for i in range(len(self.s)//2):
            tmp = self.s[i]
            self.s[i] = self.s[len(self.s)-i-1]
            self.s[len(self.s)-i-1] = tmp
        print(self.s)
# 测试
attri = ["H","a","n","n","a","h"]
result = Solution(attri)
result.reverseString()

# 解法2
# 来源于 https://leetcode-cn.com/problems/reverse-string/solution/shuang-zhi-zhen-qing-song-gao-ding-by-jamiechen_-2/
# 双指针解法。速度更快。
class Solution:
    def __init__(self,s):
        self.s = s
    def reverseString(self):
        i,j=0,len(self.s)-1
        while i<=j:
            self.s[i],self.s[j]=self.s[j],self.s[i]
            i+=1
            j-=1
        print(self.s)
# 测试
attri = ["H","a","n","n","a","h"]
result = Solution(attri)
result.reverseString()