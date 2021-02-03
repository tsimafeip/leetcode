def is_palindrome(s: str) -> bool:
    cleaned_str = [ch.lower() for ch in s if ch.isalpha() or ch.isnumeric()]
    for i, ch in enumerate(cleaned_str):
        if ch != cleaned_str[-(i + 1)]:
            return False
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome(""))
print(is_palindrome("car!"))
