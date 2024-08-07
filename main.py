import string


def main():
    book_name = "frankenstein"
    book_path = f"books/{book_name}.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of books/{book_name}.txt ---")
    print(f"{num_words} words found in the document\n")

    letter_count = get_char_count(text)
    print_sorted_letters(letter_count)

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
    return letter_count


def print_sorted_letters(letter_dict):
    letters = [{"letter": l, "count": c} for
               l, c in letter_dict.items()]
    letters.sort(reverse=True, key=sort_on)
    for letter in letters:
        print(f"The \'{letter['letter']}\' character was found {letter['count']} times")


def sort_on(my_dict):
    return my_dict["count"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
