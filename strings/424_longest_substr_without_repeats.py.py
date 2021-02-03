def get_char_index(ch: str) -> int:
    return ord(ch) - ord('A')


def character_replacement(s: str, k: int) -> int:
    max_repeat = 0
    counter = [0 for _ in range(26)]
    left = 0
    for right in range(len(s)):
        counter[get_char_index(s[right])] += 1
        max_repeat = max(max_repeat, counter[get_char_index(s[right])])
        if right - left + 1 > max_repeat + k:
            counter[get_char_index(s[left])] -= 1
            left += 1
    return min(max_repeat + k, len(s))


print(character_replacement("ABAB", 2))
print(character_replacement("AAAA", 2))
