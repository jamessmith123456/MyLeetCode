# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:57:56 2019

@author: ZhuangChi
"""
"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表
示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:
输入: 3
输出: "III"

示例 2:
输入: 4
输出: "IV"

示例 3:
输入: 9
输出: "IX"

示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""



"""
执行结果：通过
执行用时 :60 ms, 在所有 Python 提交中击败了31.70%的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了31.69%的用户
class Solution(object):
    def intToRoman(self,num):
        s = ['I','V','X','L','C','D','M']
        n = [1,5,10,50,100,500,1000]
        
        result = []
        while num != 0:         
            if num == 4:
                result += 'IV'
                num = num - 4
            elif num == 9:
                result += 'IX'
                num = num - 9
            elif 40<=num<=49:
                result += 'XL'
                num = num - 40
            elif 90<=num<=99:
                result += 'XC'
                num = num - 90                
            elif 400<=num<=499:
                result += 'CD'
                num = num - 400  
            elif 900<=num<=999:
                result += 'CM'
                num = num - 900
            else:
                index = 0
                for i in range(len(n)):
                    if n[i]<=num:
                        index = i      
                count = num//n[index]
                for i in range(count):
                    result += s[index]
                num = num%(n[index])
        return ''.join(result)
"""            

            
        