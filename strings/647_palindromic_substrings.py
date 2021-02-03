def check_str_around_center(s: str, l: int, r: int):
    res = 0

    while l >= 0 and r < len(s):
        if s[l] != s[r]:
            break

        l -= 1
        r += 1
        res += 1
    return res


def count_palindromic_substrings(s: str):
    global_res = 0

    for i in range(len(s)):
        global_res += check_str_around_center(s, i, i)
        global_res += check_str_around_center(s, i, i + 1)
    return global_res


def count_palindromic_substrings_with_matrix(s: str) -> int:
    if not s:
        return 0

    res = 0
    dp_matrix = [[False for j in range(len(s))] for i in range(len(s))]

    for i in range(len(s)):
        dp_matrix[i][i] = True
        res += 1

    for i in range(0, len(s) - 1):
        dp_matrix[i][i + 1] = (s[i] == s[i + 1])
        res += dp_matrix[i][i + 1]

    for step in range(3, len(s) + 1):
        i = 0
        j = i + step - 1
        while j < len(s):
            dp_matrix[i][j] = dp_matrix[i + 1][j - 1] and s[i] == s[j]
            res += dp_matrix[i][j]
            j += 1
            i += 1
    return res


print(count_palindromic_substrings('aaaaa'))
print(count_palindromic_substrings('abc'))
