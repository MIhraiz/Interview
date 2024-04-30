from typing import List


def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(nums)):
            dfs(i, target - nums[i], path + [nums[i]])

    dfs(0, target, [])
    return result


arr = [1, 2, 3]
target = 4

print(combinationSum(arr, target))

