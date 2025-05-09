from stats import get_word_count
from stats import get_letter_count
from stats import get_sorted
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    list_letter_count = []
    the_file_path = sys.argv[1]
    the_file_contents = get_book_text(the_file_path)
    num_words = get_word_count(the_file_contents)
    the_letter_count = get_letter_count(the_file_contents)
    list_letter_count = get_sorted(the_letter_count)
    #Print report 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {the_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in list_letter_count:
        if dictionary['char'].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")
main()


