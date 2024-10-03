def main():
    book_path = "books/frankenstein.txt"
    create_book_report(book_path)

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def count_words(text):
    word_array = text.split()
    return len(word_array)


def count_characters(text):
    character_counts = {}
    lower_text = text.lower()
    for s in lower_text:
        if s.isalpha():
            if s in character_counts:
                character_counts[s] += 1
            else:
                character_counts[s] = 1

    sorted_char_count = dict(sorted(character_counts.items(), key=lambda item: item[1], reverse=True))

    return sorted_char_count


def create_book_report(book_path):
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")

main()

