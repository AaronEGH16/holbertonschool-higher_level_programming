#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence and sentence != "":
        letter = sentence[0]
    else:
        return lenght, None
    return lenght, letter
