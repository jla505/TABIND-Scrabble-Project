
# TABIND Scrabble Project

This project aims to generate all possible valid English words that can be formed using the letters "tabind". The program reads a local dictionary file, generates permutations of the given letters, and filters out valid words.

## Features

- Generates all possible permutations of the letters "tabind".
- Filters out valid English words using a local dictionary file.
- Outputs the valid words in alphabetical order.

## Prerequisites

- Python 3.x

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/jla505/TABIND-Scrabble-Project.git
cd TABIND-Scrabble-Project
```

### Download the Dictionary File

Download the `words_alpha.txt` file from [this GitHub repository](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) and save it in the project directory.

Alternatively, you can use the following command to download it directly:

```sh
curl -O https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
```

### Running the Program

```sh
python main.py
```

## Program Explanation

The program performs the following steps:

1. **Load Words from Local Dictionary File**:
    - Reads words from `words_alpha.txt` and loads them into a set for quick lookup.

2. **Generate Permutations**:
    - Uses `itertools.permutations` to generate all possible permutations of different lengths from the given letters.

3. **Filter Valid Words**:
    - Intersects the generated permutations with the set of valid words to filter out valid English words.

4. **Sort and Output**:
    - Sorts the valid words alphabetically and prints them.

### Example Output

When you run the program, you will get an output similar to:

```
ab
abd
abdi
...
tab
tabi
...
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue in this repository.

``` 
