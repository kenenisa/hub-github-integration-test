# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start,end):
            print(start,end)
            if start > end:
                return -1
            mid = (start+end)//2
            
            if nums[mid] == target:
                return mid
            
            
        
            if nums[mid] >= nums[start]:
                if nums[start] <= target <nums[mid]:
                    return binarySearch(start,mid-1)
                return binarySearch(mid+1,end)
            if nums[mid] < target <= nums[end]:
                return binarySearch(mid+1,end)
            return binarySearch(start,mid-1)
            
        return binarySearch(0,len(nums)-1)