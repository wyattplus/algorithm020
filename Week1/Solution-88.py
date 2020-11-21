# 时间复杂度：O（m+n）
# 空间复杂度：O（1）
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 参考俩个链表合并，这题可以从后向前迭代比较，减少使用空间
        # 1.定义nums1，nums2的尾部下标，以及结果集的下标位置
        len1 = m - 1
        len2 = n - 1
        len = m + n - 1
        # 2.迭代2个数组
        while len1 >= 0 and len2 >= 0:
            # 3.判断尾部数值较大，较的从后向前填充
            if nums1[len1] > nums2[len2]:
                nums1[len] = nums1[len1]
                len1 -= 1
            else:
                nums1[len] = nums2[len2]
                len2 -= 1
            # 4.结果集的指针前移一位
            len -= 1
        # 5. while跳出时，必有一个数组为空。但只需要将nums2剩余拷贝至nums1即可（若为len2 = -1，则无所谓）
        nums1[:len2 + 1] = nums2[:len2 + 1]
