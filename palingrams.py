"""Find and display all of the palingrams in a dictionary, a palingram is a phrase which
reads the same way forwards and backwards such as 'nurses run'. """
from load_dictionary import load_file
import time


start_time = time.time()
# Read the dictionary into a list
file_name = '2of4brif.txt'
word_list = load_file(file_name)


def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words_list = set(word_list)
    for word in words_list:

        # Get the length of the word and reverse it
        end = len(word)
        reverse = word[::-1]

        # Only interested in words longer than one letter
        if end > 1:
            for i in range(end):
                # Check if a reveresed word fragment is connected to a
                # Palindromic sequence

                if word[i:] == reverse[:end-i] and reverse[end-i:] in words_list:
                    pali_list.append((word, reverse[end-i:]))
                if word[:i] == reverse[end-i:] and reverse[:end-i] in words_list:
                    pali_list.append((reverse[:end-i], word))
    return pali_list


palingrams = find_palingrams()
# Sort palingrams on the first word
palingrams_sorted = sorted(palingrams)

# Display a list of the palingrams
print(f"The number of palingrams = {len(palingrams)}")
for x in palingrams_sorted:
    print(x)

# Get the total run time
end_time = time.time()
total_time = end_time - start_time
print(f"Runtime for this program was {total_time} seconds")
