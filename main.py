def get_book_text(books):

    with open(books) as f:
    # do something with f (the file) here

    # f is a file object
     file_contents = f.read()
     return file_contents
    
def main(get_book_text):
   book_path = "books/frankenstein.txt"
   book_text = get_book_text(book_path)
   print(book_text)
main(get_book_text)