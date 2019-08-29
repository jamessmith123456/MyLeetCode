# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:09:31 2019

@author: ZhuangChi
"""

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


"""
执行结果：通过
执行用时 :92 ms, 在所有 Python 提交中击败了20.04%的用户
内存消耗 :11.7 MB, 在所有 Python 提交中击败了23.05%的用户
class Solution(object):
    def isPalindrome(self,x):
        x_list = list(str(x))
        
        if x_list[::-1] == x_list:
            return True
        else:
            return False
"""

"""
上面的操作多余了  其实不需要转化为list str同样具有[::-1]这种写法
"""


#进阶版：不将其转化为字符串

#思想：计算这个数是几位数 然后算首尾对应位的余数 来比较是否是回文数
 class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x%10==x:
            return True
        i=0
        j=0
        while x//(10**j)!=0:
            j=j+1
        j=j-1       
        while i<j:
            x1=x//(10**i)%10
            x2=x//(10**j)%10
            if x1!=x2:
                return False
            i+=1
            j-=1
        return True
        



      
                