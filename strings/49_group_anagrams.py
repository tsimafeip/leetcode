from typing import List
from collections import defaultdict


def group_anagrams_via_sorting(strs: List[str]) -> List[List[str]]:
    group_dict = defaultdict(list)
    for s in strs:
        sorted_s = str(sorted(s))
        group_dict[sorted_s].append(s)
    return list(group_dict.values())


def group_anagrams_via_counting(strs: List[str]) -> List[List[str]]:
    group_dict = defaultdict(list)
    for s in strs:
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        group_dict[tuple(counter)].append(s)
    return list(group_dict.values())


case_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
case_2 = [""]
case_3 = ["a"]
assert group_anagrams_via_sorting(case_1) == group_anagrams_via_counting(case_1)
assert group_anagrams_via_sorting(case_2) == group_anagrams_via_counting(case_2)
assert group_anagrams_via_sorting(case_3) == group_anagrams_via_counting(case_3)
