from typing import Tuple


def check_str_around_center(s: str, l: int, r: int, final_l: int, final_r: int) -> Tuple[int, int]:
    res_l, res_r = 0, 0

    while l >= 0 and r < len(s):
        if s[l] != s[r]:
            break

        res_l, res_r = l, r
        l -= 1
        r += 1
    return (res_l, res_r) if res_r - res_l > final_r - final_l else (final_l, final_r)


def longest_palindromic_substring(s: str) -> str:
    l, r = 0, 0

    for i in range(len(s)):
        l, r = check_str_around_center(s, i, i, l, r)
        l, r = check_str_around_center(s, i, i + 1, l, r)
    return s[l:r + 1]


print(longest_palindromic_substring('aaaaa'))
print(longest_palindromic_substring('abc'))
