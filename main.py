def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
