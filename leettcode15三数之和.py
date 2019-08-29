# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:12:35 2019

@author: ZhuangChi
"""

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


"""
比如result=[[1,2,4],[2,1,4],[4,2,1]]
原本想的是利用上一题的set()来对这个result进行去重
结果发现好像不可以 会报出：TypeError: unhashable type: 'list'这种错误

result = [1,2,3,4]
set(result) 输出：{1，2，3，4} 这是没问题的
"""



"""
Python中list的复制及深拷贝与浅拷贝探究
在Python中，经常要对一个list进行复制。对于复制，自然的就有深拷贝与浅拷贝问题。深拷贝与浅拷贝的区别在于，
当从原本的list复制出的list之后，修改其中的任意一个是否会对另一个造成影响，即这两个list在内存中是否储存在同一个区域，
这也是区分深拷贝与浅拷贝的重要依据。接下来我们就针对Python中list复制的几种方法，来探究一下其是属于深拷贝还是浅拷贝。
弄清楚这个问题，有助于我们在编程中规避错误，减少不必要的调试时间。

1.非拷贝方法--直接赋值
a=[1,2,3,4]
b=a
b[0]=5  b:[5,2,3,4]  a:[5,2,3,4]


2.浅拷贝的几种方法
1.copy()方法
old = [1,[1,2,3],3]
new = old.copy()
print('Before:')
print(old)   [1,[1,2,3],3]
print(new)   [1,[1,2,3],3]
new[0] = 3   
new[1][0] =3   
print('After:')
print(old)    [3,[3,2,3],3]
print(new)    [3,[3,2,3],3]
对于list的第一层，是实现了深拷贝，但对于嵌套的list，仍然是浅拷贝。这其实很好理解，内层的list保存的是地址，
复制过去的时候是把地址复制过去了。嵌套的list在内存中指向的还是同一个。

2.使用列表生成式
使用列表生成式产生新列表也是一个浅拷贝方法，只对第一层实现深拷贝。
old = [1,[1,2,3],3]
new = [i for i in old]
print('Before')
print(old)   [1,[1,2,3],3]
print(new)   [1,[1,2,3],3]
new[0] = 3
new[1][0] = 3
print('After')
print(old)   [3,[1,2,3],3]
print(new)   [3,[1,2,3],3]

3.使用for循环遍历
通过for循环遍历，将元素一个个添加到新列表中。这也是一个浅拷贝方法，只对第一层实现深拷贝。
old = [1,[1,2,3],3]
new = []
for i in range(len(old)):
    new.append(old[i])
print('Before:')
print(old)   [1,[1,2,3],3]
print(new)   [1,[1,2,3],3]
new[0] = 3
new[1][0] = 3
print('After:')
print(old)   [3,[1,2,3],3]
print(new)   [3,[1,2,3],3]

4.使用切片
通过使用[:]切片，可以浅拷贝整个列表。同样的，只对第一层实现深拷贝。
old = [1,[1,2,3],3]
new = old[:]
print('Before:')
print(old)   [1,[1,2,3],3]
print(new)   [1,[1,2,3],3]
new[0] = 3
new[1][0] = 3
print('After:')
print(old)   [3,[1,2,3],3]
print(new)   [3,[1,2,3],3]



深拷贝的实现：
如果用deepcopy()方法，则无论多少层，无论怎样的形式，得到的新列表都是和原来无关的，这是最安全最清爽最有效的方法。
使用时，要导入copy。
import copy
old = [1,[1,2,3],3]
new = copy.deepcopy(old)
print('Before:')
print(old)
print(new)
new[0] = 3
new[1][0] = 3
print('After:')
print(old)
print(new)
"""
class Solution(object):
    def threeSum(self, nums):
        nums1 = nums
        nums2 = nums
        nums3 = nums
        
        result = []
        for i in range(len(nums1)):
            for j in range(i+1,len(nums2)):
                for k in range(j+1,len(nums3)):
                    if (nums1[i]+nums2[j]+nums3[k])==0:
                        result.append([nums1[i],nums2[j],nums3[k]])
        
        result_set = []
        index = []
        for i in range(len(result)):
            temp = set(result[i])
            logo = False
            if result_set != []:
                for j in result_set:
                    if temp == j:
                       logo = False #只要有一个是相等的 就说明重复 置logo为False 且break跳出循环
                       break
                    else:
                       logo = True
                if logo == True:
                    result_set.append(temp)
                    index.append(i)
            else: #result_set == []
                result_set.append(temp)
                index.append(i)
        
        result_F = []
        for i in index:
            result_F.append(result[i])
        return result_F
    
"""
下面这种超出时间限制
"""    
class Solution(object):
    def threeSum(self, nums):
        nums1 = nums
        nums2 = nums
        nums3 = nums
        
        result = []
        for i in range(len(nums1)):
            for j in range(i+1,len(nums2)):
                for k in range(j+1,len(nums3)):
                    if (nums1[i]+nums2[j]+nums3[k])==0:
                        if [nums1[i],nums2[j],nums3[k]] in result:
                            pass
                        elif [nums1[i],nums3[k],nums2[j]] in result:
                            pass
                        elif [nums2[j],nums1[i],nums3[k]] in result:
                            pass
                        elif [nums2[j],nums3[k],nums1[i]] in result:
                            pass
                        elif [nums3[k],nums1[i],nums2[j]] in result:
                            pass
                        elif [nums3[k],nums2[j],nums1[i]] in result:
                            pass
                        else:
                            result.append([nums1[i],nums2[j],nums3[k]])
        

        return result


"""
a = [4,4,4,3,2,1,1,1]
a.sort() 啥也不输出 但是现在a变为[1,1,1,2,3,4,4,4]
如果是降序，则为a.sort(reverse=True)
"""

"""
下面这种写法仍然超时

"""
class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        
        result = []
        for i in range(len(nums)):
            if nums[i]<=0:
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]<=0:
                        for k in range(j+1,len(nums)):
                            if nums[i]+nums[j]+nums[k] == 0:
                                if [nums[i],nums[j],nums[k]] in result:
                                    pass
                                elif [nums[i],nums[k],nums[j]] in result:
                                    pass
                                elif [nums[j],nums[i],nums[k]] in result:
                                    pass
                                elif [nums[j],nums[k],nums[i]] in result:
                                    pass
                                elif [nums[k],nums[i],nums[j]] in result:
                                    pass
                                elif [nums[k],nums[j],nums[i]] in result:
                                    pass
                                else:
                                    result.append([nums[i],nums[j],nums[k]])
                                    break
                    else:
                        break
            else:
                break
        return result




"""
我自己是想不出来了 下面是看别人的代码：
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        算法思路：最外层控制一个元素的循环，
                内层用双指针，一个从头到尾扫描，另一个从尾到头扫描，判断三个元素的值之和是否为零
                
        注意：相同的元素需要跳过
        '''
        # 对列表进行排序
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            # 如果出现最小元素为正数，则不存在和为0的情况，直接返回
            if nums[k] > 0:
                break
            # 如果出现第一个元素重复的情况，为避免重复结果，跳过后续执行
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 定义接下来的两个元素的双指针
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    # 跳过重复元素
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    # 跳过重复元素
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    # 当出现元素满足条件是，将结果加入到列表
                    res.append([nums[k], nums[i], nums[j]])
                    # 接着更新索引（注意跳过相同元素）
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res