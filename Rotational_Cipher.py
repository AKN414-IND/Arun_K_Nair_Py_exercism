def rotate(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            a = 65 if char.isupper() else 97
            s = (ord(char) - a + key) % 26 + a
            result += chr(s)
        else:
            result += char
    return result
