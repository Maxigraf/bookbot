def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_counts = count_characters(file_contents)
        print(char_counts)

def calculate_number_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    result = {}

    for ch in text.lower():
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    return result

main()