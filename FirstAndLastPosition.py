from typing import List


def binarySearch(nums: List[int], target: int, lookLeft: bool) -> int:
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            ans = mid
            if lookLeft:
                right = mid - 1
            else:
                left = mid + 1
    return ans


def findTargetIndeciesBS(nums: List[int], target: int) -> List[int]:
    firstIndex = binarySearch(nums, target, True)
    if firstIndex == -1:
        return [-1, -1]
    lastIndex = binarySearch(nums, target, False)
    if lastIndex == firstIndex:
        return [-1, -1]
    return [firstIndex, lastIndex]


input1 = [1, 1, 3, 4, 5, 6, 7]
input2 = 7

print(findTargetIndeciesBS(input1, input2))
