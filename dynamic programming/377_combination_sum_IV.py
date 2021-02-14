from typing import List, Dict, Set


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self._bottom_up(nums=nums, target=target)
        return self._top_down(nums=set(nums), remainder=target, cache=dict())

    def _bottom_up(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        # if local target during bottom up will be equal to current number, then one unique sequence has to be added
        dp[0] = 1

        for local_target in range(1, target + 1):
            for num in nums:
                if num > local_target:
                    continue
                dp[local_target] += dp[local_target - num]
        return dp[target]

    def _top_down(self, nums: Set[int], remainder: int, cache: Dict[int, int]) -> int:
        if remainder < 0:
            return 0

        if remainder in cache:
            return cache[remainder]

        local_res = 0

        if remainder in nums:
            local_res += 1

        for num in nums:
            local_res += self._top_down(nums, remainder - num, cache)

        cache[remainder] = local_res

        return cache[remainder]


sol = Solution()
print(sol.combinationSum4(nums=[1, 2, 3], target=4))
