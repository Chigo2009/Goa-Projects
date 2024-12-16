def custom_split(string, delimiter=" "):
    result = []
    current_word = ""
    
    for char in string:
        if char == delimiter:
            if current_word:  # თუ სიტყვა არსებობს, დაამატე ის სიაში
                result.append(current_word)
                current_word = ""  # დააბრუნე ცარიელ მდგომარეობაში
        else:
            current_word += char  # დაამატე სიმბოლო სიტყვას
            
    if current_word:  # თუ ბოლო სიტყვა დარჩა, დაამატე ის სიაში
        result.append(current_word)
    
    return result
text = "This is a test"
result = custom_split(text)
print(result)


def custom_join(iterable, delimiter=""):
    result = ""
    for i, item in enumerate(iterable):
        result += item
        if i < len(iterable) - 1:  # მხოლოდ უკანასკნელ ელემენტზე არ დავამატოთ delimiter
            result += delimiter
    return result


words = ['This', 'is', 'a', 'test']
result = custom_join(words, delimiter=" ")
print(result)


def custom_replace(string, old, new):
    result = ""
    i = 0
    
    while i < len(string):
        # თუ ვპოულობთ old-ს, ჩავსვათ new და გადავიდეთ old-ის სიგრძეზე
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    
    return result

text = "I have a cat. My cat is cute."
result = custom_replace(text, "cat", "dog")
print(result)

