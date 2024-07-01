import itertools

# Load words from the local dictionary file
def load_words(file_path):
    with open(file_path, 'r') as file:
        valid_words = set(file.read().split())
    return valid_words

def find_words(letters, valid_words):
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

# Path to the local dictionary file
dictionary_file_path = 'words_alpha.txt'

# Load the dictionary
valid_words = load_words(dictionary_file_path)

# Letters provided
letters = "tabind"

# Find and print valid words
valid_words_list = find_words(letters, valid_words)
for word in valid_words_list:
    print(word)

