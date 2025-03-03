import sys
from stats import (
    get_num_words,
    get_num_characters,
    build_list_of_dictionaries
) 
  
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path) #get the text of book
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text) #count the characters in the book
    chars_sorted_list = build_list_of_dictionaries(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(path):
    with open(path) as f: 
        file_contents = f.read()
        return file_contents

def print_report(book_path,num_words,chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #PRINT THE SORTED LIST IN THE DESIRED FORMAT
    for i in range(len(chars_sorted_list)):
        print(f"{chars_sorted_list[i]['characters']}: {chars_sorted_list[i]['count']}")

    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    main()