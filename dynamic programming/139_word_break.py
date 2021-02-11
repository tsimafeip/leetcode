from typing import List, Dict, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.word_break_top_down(words=set(wordDict), target_word=s, cache=dict())
        return self.word_break_bottom_up(words=set(wordDict), target_word=s)

    # recursion_tle
    def word_break_recursion_tle(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True

        for word in wordDict:
            if len(word) > len(s):
                continue

            if s[:len(word)] == word:
                if self.word_break_recursion_tle(wordDict=wordDict, s=s[len(word):]):
                    return True

        return False

    def word_break_top_down(self, words: Set[str], target_word: str, cache: Dict[str, bool]) -> bool:
        if target_word in words:
            return True

        if target_word in cache:
            return cache[target_word]

        for i in range(1, len(target_word)):
            left_substr = target_word[:i]

            if left_substr in words and self.word_break_top_down(words=words, target_word=target_word[i:], cache=cache):
                cache[target_word] = True

        if target_word not in cache:
            cache[target_word] = False

        return cache[target_word]

    def word_break_bottom_up(self, words: Set[str], target_word: str) -> bool:
        dp = [False] * (len(target_word) + 1)
        dp[0] = True

        for i in range(1, len(target_word) + 1):
            for j in range(0, i):
                if target_word[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]


sol = Solution()

print(sol.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak(
    s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
