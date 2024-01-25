def merge_sorted_arrays(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    temp_arr = []
    index_1 = 0
    index_2 = 0

    while index_1 < m and index_2 < n:
        if nums1[index_1] <= nums2[index_2]:
            temp_arr.append(nums1[index_1])
            index_1 += 1
        else:
            temp_arr.append(nums2[index_2])
            index_2 += 1

    while index_1 < m:
        temp_arr.append(nums1[index_1])
        index_1 += 1

    while index_2 < n:
        temp_arr.append(nums2[index_2])
        index_2 += 1

    nums1[:] = temp_arr[:n + m]
