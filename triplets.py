# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def list2dict(x):
            a = dict()
            for i in x:
                if i not in a:
                    a[i] = 1
                else: a[i]+= 1
            return a
        ans = set()
        ft = list2dict(nums)
        if 0 in ft:
            if (ft[0] >=3):
                ans.add((0,0,0))
            else:
                for each in ft:
                    if (-each in ft and each != 0): ans.add(tuple(sorted((each,0,-each))))
        for each in ft:
            if each!=0:
                for other in ft:
                    another = -(each+other)
                    if (another in ft):
                        if(each != other and other != another and another != each) or (each == other and ft[each]>1) or (each == another and ft[each]>1) or (other == another and ft[other]>1):
                            ans.add(tuple(sorted((each, other,another ))))

        return ans
