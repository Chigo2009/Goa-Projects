def longest_word(string_of_words):
    """
    dab sodkbapskd paksdb opskdaops dbok abd red whitblue golde blue
    bla lbal baslbdal sdabksdlas kdbalkd;lb sa;ldklab; skdb;lask dlab;skdl;abskdl;a
    aloskdbaskdlkas kbaks dlbksdabs kdabksda
    sb askdaskdpasdpkabskdbaks db a
    red 
    """
    words = string_of_words.split()
    longest = ""
    for word in words:
        if len(word) >= len(longest):
            longest = word
    return longest


print(longest_word("red white blue"))  
print(longest_word("red blue gold"))  