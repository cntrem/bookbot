from stats import num_words, num_chars
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def main(filename):
    book_text = get_book_text(filename)
    my_dict = num_chars(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filename)
    print("----------- Word Count ----------")
    print("Found", num_words(book_text), "total words")
    print("--------- Character Count -------")
    for char, count in my_dict.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        book_file = sys.argv[1]
        main(book_file)
    else:
        raise(ValueError("Usage: python3 main.py <path_to_book>"))