# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:57:52 2019

@author: ZhuangChi
"""

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.





num_s = [1,2,3]
num_s[2:-1]    []
num_s[1:2]     [2]
num_s[0:3]     [1,2,3]






"""
执行结果：通过
执行用时 :96 ms, 在所有 Python 提交中击败了6.92%的用户
内存消耗 :11.6 MB, 在所有 Python 提交中击败了33.84%的用户
"""

class Solution(object):
    def romanToInt(self,s):
        num_s = []
        for i in s:
            if i=='I':
                num_s.append(1)
            if i=='V':
                num_s.append(5)
            if i=='X':
                num_s.append(10)
            if i=='L':
                num_s.append(50)
            if i=='C':
                num_s.append(100)
            if i=='D':
                num_s.append(500)
            if i=='M':
                num_s.append(1000)
            
        for i in range(len(num_s)):
            if len(s)-i-1>=1:
                current = num_s[i]
                after = num_s[i+1:len(num_s)]   #num_s[i+1:-1]这样写是不对的
                
                if current < max(after):
                    num_s[i] = -num_s[i]
            
        result = 0
        for i in num_s:
            result += i
        
        return result







"""
下面是网上的比较快的写法  实际跟我的想法是一样的啦  只不过别人用字典来进行映射 这样很快 
而且只要每个数字与右手边数字进行判断即可  不需要每个数字与他右边的所有数字进行判断

"""



"""
执行结果：
显示详情执行用时 :104 ms, 在所有 Python 提交中击败了5.46%的用户
内存消耗 :11.8 MB, 在所有 Python 提交中击败了16.03%的用户
"""
"""
好吧 实际上也不是很快...应该是万盏服务器波动的原因 因为第二次提交速度又变了...
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans
    