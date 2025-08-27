from stats import word_count

def get_book_text(books):

    with open(books) as f:
    # 

    # f is a file object
     file_contents = f.read()
     return file_contents
    


def main():
   book_path = "books/frankenstein.txt"
   book_text = get_book_text(book_path)
   num_words = word_count(book_text)
   print(f"{num_words} words found in the document")
main()
