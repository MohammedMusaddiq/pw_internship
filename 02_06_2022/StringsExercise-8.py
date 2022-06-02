# 8. Write a Python function that takes a list of words and returns the length of the longest one.

list_of_words = input("Enter words separated by a space: ")
list_of_words = list_of_words.split()


def find_longest_world_len(lst):
    longest_word = ''
    longest_word_len = 0

    for i in lst:
        if longest_word_len < len(i):
            longest_word_len = len(i)
            longest_word = i
    return print(f'the longest word is "{longest_word}" with length "{longest_word_len}"')


find_longest_world_len(list_of_words)
