def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)

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

    output = []

    for item in result:
        output.append({"name": item, "num": result[item]})

    return output

def sort_on(dict):
    return dict["num"]

def print_report(text):
    number_of_words = calculate_number_of_words(text)
    char_counts = count_characters(text)

    char_counts.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print()

    for char in char_counts:
        if char["name"] >= 'a' and char["name"] <= 'z':
            print(f"The '{char["name"]}' character was found {char["num"]} times")

    print("--- End report ---")

main()