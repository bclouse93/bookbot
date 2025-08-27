from stats import num_words
    
def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words
     #print (f"{word_count} words found in the document")   


