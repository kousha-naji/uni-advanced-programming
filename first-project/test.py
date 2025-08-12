vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def vowel_finder(word):
    vowels_in_word = [char for char in word.lower() if char in vowels]
    return vowels_in_word == vowels

try:
    filename = input("Enter file name: ")
    with open(filename, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
    exit(1)

words_found = [word for word in content.split() if vowel_finder(word)]

print(words_found if words_found else "No matching words found.")