def is_valid_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()
print(is_valid_pin("1234"))   
print(is_valid_pin("12345"))  
print(is_valid_pin("a234"))  

