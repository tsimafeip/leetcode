def is_valid(s: str) -> bool:
    stack = []
    closing_to_open_dict = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in closing_to_open_dict:
            # check open-to-close type matching
            open_bracket = stack.pop() if stack else "!"
            if open_bracket != closing_to_open_dict[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
