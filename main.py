import sys
from stats import char_count, report, word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path to book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    wc = word_count(text)
    chars = char_count(text)
    print(chars)

    output = "============ BOOKBOT ============\n"
    output += f"Analyzing book found at {filepath}...\n"
    output += "----------- Word Count ----------\n"
    output += f"Found {wc} total words\n"
    output += "--------- Character Count -------"
    print(output)
    report(chars)

main()