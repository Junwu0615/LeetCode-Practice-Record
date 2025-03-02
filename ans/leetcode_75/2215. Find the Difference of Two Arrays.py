class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        del_list = list(set(nums1)&set(nums2))
        for i in del_list:
            while i in nums1:
                nums1.remove(i)
            while i in nums2:
                nums2.remove(i)
        else:
            return [list(set(nums1)), list(set(nums2))]