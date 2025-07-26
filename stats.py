def count_words_total(text):
    """Count the number of words in a given string"""
    separated = text.split()   
    return len(separated)

def count_words(text):
    """Return a dictionary with the number of words in a given text"""
    separated = text.split()
    word_map = {}
    for word in separated:
        if word_map.get(word):
            word_count = word_map[word] + 1
        else:
            word_count = 1
        word_map[word] = word_count
    return word_map

def count_characters(text):
    """Return a dictionary with all the character counts"""
    char_map = {}

    for _c in text:
        lower_c = _c.lower()
        if char_map.get(lower_c):
            char_count = char_map[lower_c] + 1
        else:
            char_count = 1
        char_map[lower_c] = char_count
    
    return char_map