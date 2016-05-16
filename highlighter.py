from colors import Colors
import re

def highlight_with_to(sentence, color = Colors.UNDERLINE):
    regex = re.compile(r"\w+ to \w+", re.IGNORECASE)
    phrase = regex.findall(sentence)[0]
    return sentence.replace(phrase, color + phrase + Colors.ENDC)

def highlight_with_brackets(sentence):
    re.sub('{[\w\s]+}', Colors.UNDERLINE + '\1' + Colors.ENDC, sentence)