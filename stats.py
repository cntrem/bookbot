def num_words(book):
    a = book.split()
    return len(a)

def num_chars(book):
    char_counts = {}
    characters_to_count = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    for char in book:
       theChar = char.lower()
       if theChar in characters_to_count:
           char_counts[theChar] = char_counts.get(theChar, 0) + 1    
    return char_counts

        