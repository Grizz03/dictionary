import json
from difflib import get_close_matches

data = json.load(open('data.json'))

word = input('Enter word: ')

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s instead? Press Y for yes and N for no: ' % get_close_matches(w, data.keys())[0]).lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word does not exist in the archive."
        else:
            return "We did not understand your entry."
    else:
        return 'The word does not exist in the archive.'



print(translate(word))


