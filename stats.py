def word_count(book_text):
    # Splits the input text into a list of words using whitespace as a delimiter.
    words = book_text.split()
    # Calculates the total number of items (words) in the list.
    num_words = len(words)
    # Returns the final word count.
    return num_words
       

def get_char_count(book_text):
    # Converts the entire book text to lowercase to ensure 'A' and 'a' are counted as the same character.
    char_count = book_text.lower()
    # Initializes an empty dictionary to store character counts.
    char_dict={}
    # Loops through each character in the lowercased text.
    for char in char_count: 
        # If the character is already a key in the dictionary, increment its value (count).
        if char in char_dict:
            char_dict[char] += 1
        # If the character is not in the dictionary, add it as a new key with a value of 1.
        else:
            char_dict[char] = 1
    # Returns the dictionary containing all characters and their counts.
    return char_dict

def sort_key(d):
    # A helper function that returns the value of the "num" key from a dictionary.
    # This is used by the .sort() method to know what to sort by.
    return d["num"]

def chars_dict_to_sorted_list(char_dict):
    # Initializes an empty list to hold the dictionaries for sorting.
    sorted_list = []
    # Loops through each character (key) in the input dictionary.
    for char in char_dict:
        # Checks if the character is an alphabetic letter.
        if char.isalpha() and 'a' <= char <= 'z':
            # If it's a letter, create a new dictionary for it and append it to the list.
            sorted_list.append({"char": char, "num": char_dict[char]})
    # Sorts the list of dictionaries in-place.
    # `reverse=True` sorts from highest to lowest.
    # `key=sort_key` tells sort to use the value from our helper function for comparison.
    sorted_list.sort(reverse=True, key=sort_key)
    # Returns the newly sorted list.
    return sorted_list
