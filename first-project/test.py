def vowel_finder(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_in_word = [char for char in word.lower() if char in vowels]
    if vowels_in_word == vowels:
        words_found.append(word)
    return ''

words_found = []


try:
    with open('ipsum.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")

words = content.split()
uppercase_words = [word.upper() for word in words]
for word in uppercase_words:
    vowel_finder(word)    

print(words_found)  