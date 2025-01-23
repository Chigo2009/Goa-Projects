def is_isogram(s: str) -> bool:
    s = s.lower()
    seen = set()
    for char in s:
        if char in seen:
            return False  
        seen.add(char)
    return True
