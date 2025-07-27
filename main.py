import sys
import stats

def main():
    """  Main program """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    num_words = stats.count_words_total(text)
    char_map = stats.count_characters(text)
    sorted_chars = stats.sort_characters(char_map)

    print ("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")

    print('============= END ===============')


def get_book_text(filepath):
    """ Returns contents of file as a string """

    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


if __name__ == '__main__':
    main()