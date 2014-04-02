direction = ('north', 'west', 'east', 'south', 'up', 'down', 'left', 'right')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('in', 'the', 'of', 'from', 'at', 'it')
noun = ('bear', 'princess', 'cabinet', 'door')
lexicon = {'direction': direction, 'verb': verb, 'stop': stop, 'noun': noun}


def scan(sentence):
    #sentence = raw_input('> ')
    result = []
    words = sentence.split()
    for word in words:
        error = False
        for types, values in lexicon.items():
            if word in values:
                b = (types, word)
                result.append(b)
                error = True
        # Check if word is an number.
        if is_number(word):
                b = ('number', int(word))
                result.append(b)
                error = True
        # Check if the word is in lexicon if not return type = error.
        if error is False:
            b = ('error', word)
            result.append(b)
    return result


def is_number(word):
    try:
        int(word)
        return True
    except ValueError:
        return False
