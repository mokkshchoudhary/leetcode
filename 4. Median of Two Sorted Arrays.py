class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int],) -> float:
        nums3 = nums1 + nums2
        sorted_nums3 = sorted(nums3)
        n = len(nums3)
        if n%2 == 0:
          i = int(n/2)
          j = int((n/2)+1)
          return(float((sorted_nums3[i-1]+sorted_nums3[j-1])/2))
        if n%2 != 0:
            i = int((n+1)/2)
            return(float(sorted_nums3[i-1]))
