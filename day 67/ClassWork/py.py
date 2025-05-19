numbers = lambda n1, n2, n3: (n1 + n2 + n3) / 3  
print(numbers(1, 4, 5))  



luwi_or_kenti = lambda number: "luwi" if number % 2 == 0 else "kenti"

positive_sum = lambda arr: sum(z for z in arr if z > 0)
find_smallest_int = lambda arr: min(arr)


count_by = lambda x, n: [x * i for i in range(1, n + 1)]