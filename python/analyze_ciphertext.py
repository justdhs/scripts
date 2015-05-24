#! /usr/bin/env python

__author__ = "justdhs@github"

import nltk


# the ciphertext goes in here, obviously:
text = ""

def nltk_processing():
    # make the cipher text computable by the NLTK
    my_text = nltk.Text(text)
    # show the unique characters in the text
    fdist = nltk.FreqDist(text)

    return fdist


# count the occurences of words in the text
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


# draw a fancy plot for the distribution of characters withing the text
def plot():
    # first, split the text into single characters
    chars = []
    for c in text:
        if c not in chars:
            chars.append(c)

    # make the ciphertext and computable by NLTK
    my_text = nltk.Text(text)
    my_text.dispersion_plot(chars)


if __name__ == '__main__':
    print("Individual characters ordered by frequency:\n", nltk_processing().keys())
    print("\nCount of individual characters:\n", frequency(text))
    print("\nCount of individual words:\n", frequency(text.split()))

    # if you want to see a fancy plot
    # for the distribution of characters withing the text,
    # uncomment the following function call
    # plot()
