def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = calculate_number_of_words(file_contents)
        print(num_words)

def calculate_number_of_words(text):
    words = text.split()
    return len(words)

main()