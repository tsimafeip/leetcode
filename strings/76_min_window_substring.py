from collections import defaultdict

from typing import Dict


class Solution:
    def _create_dict(self, t: str) -> Dict[str, int]:
        d = defaultdict(int)
        for ch in t:
            d[ch] += 1
        return d

    def minWindow(self, s: str, t: str) -> str:
        t_dict = self._create_dict(t)
        l, r, min_l, min_r = 0, 0, None, None
        window_dict = defaultdict(int)
        formed = 0

        while r < len(s):
            window_dict[s[r]] += 1

            if s[r] in t_dict and window_dict[s[r]] == t_dict[s[r]]:
                formed += 1

            while l <= r and formed == len(t_dict):
                if (min_l is None and min_r is None) or (min_r - min_l > r - l):
                    min_l, min_r = l, r

                window_dict[s[l]] -= 1

                if s[l] in t_dict and window_dict[s[l]] < t_dict[s[l]]:
                    formed -= 1

                l += 1
            r += 1
        return s[min_l:min_r + 1] if (min_l is not None and min_r is not None) else ""


sol = Solution()

print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))
print(sol.minWindow(s="a", t="a"))
