#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "justdhs@github"

# the ciphertext, obviously
text = ""


# count the occurences of words or characters in the text
def frequency(arr):
    # count each element in arr
    single_items = []
    for a in arr:
        if ((a is not "\n") and (a is not " ")):
            s = (arr.count(a), a)
            if s not in single_items:
                single_items.append(s)
        else:
            pass
    # sort the tuples in the array by their count
    single_items.sort(key=lambda tup: tup[0], reverse=True)

    return single_items


# make a list with all individual characters, as well as a count
# expects the return value of frequency(text) as its passed parameter
def individual_chars(chars_array):
    indiv_chars = []
    for c in chars_array:
        indiv_chars.append(c[1])

# Note: return value is a tuple!
    return len(indiv_chars), indiv_chars


# # draw a fancy plot for the distribution of characters within the text
# # you have to uncomment this function, and its call, to use it
# def plot():
#     import nltk
#     # first, split the text into single characters
#     # we can't reuse frequency() because we need every occurance of each character
#     chars = []
#     for c in text:
#         if c not in chars:
#             chars.append(c)
#
    # # make the ciphertext computable by NLTK
    # my_text = nltk.Text(text)
    # my_text.dispersion_plot(chars)


if __name__ == '__main__':
    f = frequency(text)
    c = individual_chars(f)
    print("\nCount of individual characters:", c[0])
    print("\nIndividual characters ordered by frequency:\n", c[1])
    print("\nCount of individual characters:\n", f)
    print("\nCount of individual words:\n", frequency(text.split()))

    # if you want to see a fancy plot
    # for the distribution of characters withing the text,
    # uncomment the following function call, as well as the function itself.
    # you need the Natural Language ToolKit installed
    # plot()
