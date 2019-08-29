# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:08:18 2019

@author: ZhuangChi
"""

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


"""
这种最不优雅的解法 不出意外地超出了时间限制
"""
class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        
        result = []
        result_index = []
        temp_diff = None
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    diff = abs(nums[i]+nums[j]+nums[k]-target)
                    if temp_diff == None:
                        temp_diff = diff
                        result = nums[i]+nums[j]+nums[k]
                        result_index = [i,j,k]
                    else:
                        if diff<temp_diff:
                            temp_diff = diff
                            result = nums[i]+nums[j]+nums[k]
                            result_index = [i,j,k]
        return result
    



"""
执行结果：通过
执行用时 :156 ms, 在所有 Python 提交中击败了30.51%的用户
内存消耗 :11.8 MB, 在所有 Python 提交中击败了25.93%的用户
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        result = []
        result_index = []
        temp_diff = None
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j<k:
                diff = abs(nums[i]+nums[j]+nums[k]-target)
                if temp_diff == None:
                    temp_diff = diff
                    result = (nums[i]+nums[j]+nums[k])
                    result_index = [i,j,k]
                else:
                    if diff<temp_diff:
                        temp_diff = diff
                        result = (nums[i]+nums[j]+nums[k])
                        result_index = [i,j,k]
                if (nums[i]+nums[j]+nums[k])==target:
                    result = (nums[i]+nums[j]+nums[k])
                    return result
                elif (nums[i]+nums[j]+nums[k])<target:
                    j+=1
                else:
                    k-=1
        
        return result