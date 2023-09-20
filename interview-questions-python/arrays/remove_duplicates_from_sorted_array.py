from typing import Tuple, Any, List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:  # Check if the list is empty
        return 0

    i = 0  # Slow-runner (pointer)
    for j in range(1, len(nums)):  # Fast-runner (pointer)
        if nums[j] != nums[i]:  # If the current number is different from the previous number
            i += 1
            nums[i] = nums[j]  # Update the next unique number's position

    return i + 1  # Return the new length of the modified list
