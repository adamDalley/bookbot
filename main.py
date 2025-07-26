import stats

def main():
    """  Main program """
    filepath = 'books/frankenstein.txt'
    frankentext = get_book_text(filepath)

    num_words = stats.count_words_total(frankentext)
    char_count = stats.count_characters(frankentext)

    print(f'{num_words} words found in the document')
    print(char_count)


def get_book_text(filepath):
    """ Returns contents of file as a string """

    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


if __name__ == '__main__':
    main()