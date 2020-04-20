"""This program uses a method called recursion to identify palindromes
These are words which read the same forwards as backwards. """
from load_dictionary import load_file

# Read in the dictionary file
file_name = '6of12.txt'
words = load_file(file_name)


def find_palindromes(word_list):
    """Find palindromes in a list of words"""
    # Initialise empty list for palindromes
    palindromes = []

    for word in word_list:

        new_word = word

        while True:
            length = len(new_word)

            # Words with 1 or 0 characters are palindromes
            if length == 0 or length == 1:
                # Append the original word instead of the chopped word
                palindromes.append(word)
                break

            # If first and last don't match then not palindrome
            if new_word[0] != new_word[length-1]:
                # Not a palindrome
                break

            else:
                # Chop the first and last character off the word
                new_word = word[1:length-1]

    return palindromes

# Display the words
palindromes = find_palindromes(words)
for palindrome in palindromes:
    print(palindrome)

