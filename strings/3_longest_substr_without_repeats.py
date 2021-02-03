def get_longest_substr_without_repeats(s: str):
    ch_dict = {}
    start_index, cur_max, max_len = 0, 0, 0
    for index, ch in enumerate(s):
        ch_index = ch_dict.get(ch, None)
        if ch_index is not None and start_index <= ch_index:
            start_index = ch_index + 1
            cur_max = index - ch_index - 1
        cur_max += 1
        ch_dict[ch] = index
        max_len = max(max_len, cur_max)
    return max_len


def sliding_window_solution(s: str):
    ch_set = set()
    max_len = 0
    l, r = 0, 0
    for r in range(len(s)):
        while s[r] in ch_set:
            ch_set.remove(s[l])
            l += 1

        ch_set.add(s[r])
        max_len = max(r - l + 1, max_len)
    return max_len


print(sliding_window_solution("abcabcbb"))
print(get_longest_substr_without_repeats("bbbbb"))
print(get_longest_substr_without_repeats("pwwkew"))
print(get_longest_substr_without_repeats(""))
print(get_longest_substr_without_repeats("dvdf"))
print(get_longest_substr_without_repeats("abba"))
