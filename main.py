import sys
from stats import count_words, get_char_number, sort_dict

def get_book_txt(book):
    with open(book) as f:
        content = f.read()
    return content

def main():
    # Explanation how to use
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Word count
    num_words = count_words(book_path)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    chars = get_char_number(book_path)
    sorted_chars = sort_dict(chars)

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
