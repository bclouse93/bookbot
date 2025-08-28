# This line imports the functions we need from our other file, stats.py
import sys
from stats import word_count, get_char_count, chars_dict_to_sorted_list

# This function takes a file path and returns all the text from that file.
def get_book_text(path):
    # 'with open(...) as f:' is the recommended way to open files in Python.
    # It automatically closes the file when you're done.
    with open(path) as f:
        # The .read() method reads the entire contents of the file into a string.
        return f.read()

# This is the main function where our program's logic will run.
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path-to-book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # Get the book's text and store it in the 'text' variable.
    text = get_book_text(book_path)
    # Use the word_count function to count the words in the book.
    num_words = word_count(text)
    # Use the get_char_count function to count each character.
    char_counts = get_char_count(text)
    # Get the character counts and sort them lsfrom highest to lowest.
    sorted_char_list = chars_dict_to_sorted_list(char_counts)

    # Start printing the report.
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") # Print a blank line for spacing.

    # Loop through each character in our sorted list.
    for item in sorted_char_list:
        # Print a line for each character, showing how many times it appeared.
        print(f"{item['char']}: {item['num']}")

    # Print the end of the report.
    print("============= END ===============")

# This is the standard way to make a Python script runnable. It calls the main() function.
main()
