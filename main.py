import itertools
import nltk
from nltk.corpus import words

# Download the word list if not already done
nltk.download('words')

# Get the set of valid words
valid_words = set(words.words())

def find_words(letters):
    # Generate all permutations of the given letters
    permutations = set(
        ''.join(p)
        for i in range(1, len(letters) + 1)
        for p in itertools.permutations(letters, i)
    )
    
    # Filter permutations to get valid words
    valid_permutations = permutations.intersection(valid_words)
    
    # Return sorted list of valid words
    return sorted(valid_permutations)

# Letters provided
letters = "tabind"

# Find and print valid words
valid_words_list = find_words(letters)
for word in valid_words_list:
    print(word)
