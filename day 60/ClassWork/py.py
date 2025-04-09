def arara_count(n):
    if n == 1:
        return "anane"

    result = 'adak ' * (n // 2)
    if n % 2 != 0:
        result += 'anane'

    return result

print(arara_count(3))  
print(arara_count(8))  