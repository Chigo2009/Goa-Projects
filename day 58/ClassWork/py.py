def lottery(s):
    numbers = ""
    seen = set()
    for char in s:
        if char.isdigit() and char not in seen:
            numbers += char
            seen.add(char)
    if numbers:
        return numbers
    else:
        return "One more run !"
    
print(lottery("HylySochea"))