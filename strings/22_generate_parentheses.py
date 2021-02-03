from typing import List


def generate_parentheses(n: int) -> List[str]:
    res_list = []

    def backward(s: str = "", l: int = 0, r: int = 0):
        if len(s) == 2 * n:
            res_list.append(s)
            return
        if l < n:
            backward(s + '(', l + 1, r)
        if r < l:
            backward(s + ')', l, r + 1)

    backward()
    return res_list


print(generate_parentheses(3))
print(generate_parentheses(2))
print(generate_parentheses(1))
