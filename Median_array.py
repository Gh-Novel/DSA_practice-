from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Get the border values of the partitions
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')

            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')

            # Check if the partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the combined length is odd
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If the combined length is even
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        # If inputs are invalid
        raise ValueError("Input arrays are not valid!")
