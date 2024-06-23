"""
Word Occurrences
Estimate: 40 minutes
Actual:   45 minutes
(Estimated time to complete: 30 minutes) Still longer than you should take.
"""
"""
File: word_occurrences.py
This program counts the occurrences of words in a user-provided string and prints the counts sorted alphabetically.
It formats the output so that the numbers are aligned in a nice column.
"""

# create a dictionary
word_counts = {}


def find_longest_word(sorted_word_counts):
    longest_word_length = 0
    for word in sorted_word_counts:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length


def count_word_occurence(words):
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

def print_word_count(sorted_word_counts, longest_word_length):
    for word, count in sorted_word_counts.items():
        print(f"{word:{longest_word_length}} : {count}")


def main():
    words = input("Text: ").lower().split()
    count_word_occurence(words)
    sorted_word_counts = dict(sorted(word_counts.items()))
    longest_word_length = find_longest_word(sorted_word_counts)
    print_word_count(sorted_word_counts, longest_word_length)


main()


