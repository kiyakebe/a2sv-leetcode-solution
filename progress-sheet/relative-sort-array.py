class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        nums1 = []
        nums2 = []
        for i in arr1:
            if i in arr2_set: nums1.append(i)
            else: nums2.append(i)
        d = Counter(nums1)

        ans = []
        for i in arr2:
            ans += [i] * d[i]
        return ans + sorted(nums2) 
















