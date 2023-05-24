import string

def is_pangram(sentence):
    sentence = sentence.lower() 
    letters = set(sentence)
    letters = set(char for char in letters if char in string.ascii_lowercase)
    return len(letters) == 26
