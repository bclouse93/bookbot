def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words
     #print (f"{word_count} words found in the document")   

def get_char_count(book_text):
    char_count = book_text.lower()
    char_dict={}
    for char in char_count: 
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
print(get_char_count("hello"))
     #print (f"{word_count} words found in the document")   
