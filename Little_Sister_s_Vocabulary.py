def add_prefix_un(word):
    return 'un'+word;


def make_word_groups(vocab_words):
    pre = vocab_words[0]
    words = vocab_words[1:]
    word_a=[pre+word for word in words]
    return pre + ' :: ' + ' :: '.join(word_a)
    
def remove_suffix_ness(word):
    if word.endswith('ness'):
        root = word[:-4]
        if root.endswith('i') and len(root) > 1 and root[-2].isalpha() and not root[-2].lower() in ['a', 'e', 'i', 'o', 'u']:
            root = root[:-1] + 'y'
        return root
    return word
    

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].rstrip(",.!?")
    verb = adjective + "en"
    return verb
