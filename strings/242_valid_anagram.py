def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = [0 for _ in range(26)]
    for s_ch, t_ch in zip(s, t):
        counter[ord(s_ch) - ord('a')] += 1
        counter[ord(t_ch) - ord('a')] -= 1

    return not any(counter)


print(isAnagram("anagram", "magrana"))
