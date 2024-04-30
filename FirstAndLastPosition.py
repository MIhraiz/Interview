from typing import List


def findTargetIndeciesBS(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left, right = mid, mid
            while left >= 0 and right < len(nums) and nums[left] == target and nums[right] == target :
                left, right = left - 1, right + 1

            while left >= 0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1
            left, right = left + 1, right - 1
            if left == right:
                return [-1, -1]
            return [left, right]

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]


input1 = [1, 1, 3, 4, 5, 7, 7]
input2 = 10

print(findTargetIndeciesBS(input1, input2))
