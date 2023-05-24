def is_isogram(word):
    word = word.replace(" ", "").replace("-", "")
    word = word.lower()
    unique_letters = set(word)
    return len(unique_letters) == len(word)
