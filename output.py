from colors import Colors
from messages import Messages
import highlighter

def draw_line(num):
    print('=' * num)

def log(message):
    console_message = ' ' + message + ' '
    message_length = len(console_message)

    draw_line(message_length)
    print(console_message)
    draw_line(message_length)

    print()

def show_congratulation():
    log(Messages.GAME_SUCCESSFULLY_COMPLETED)

def show_answered(answered):
    print(Messages.ANSWERED_WORDS % ', '.join(answered))

def show_word_usage_examples(examples, highlight):
    if not examples:
        return
    
    message = Messages.EXAMPLES_LEADING_TEXT
    print(message)

    for example in examples:
        show_word_usage_example(example, highlight, len(message) + 1)

def show_word_meanings(meanings):
    message = Messages.MEANINGS_LEADING_TEXT
    print(message)

    for meaning in meanings:
        show_word_meaning(meaning, len(message) + 1)

def show_word_meaning(meaning, leading_whitespaces=0):
    if meaning:
        message = leading_whitespaces * ' ' + Messages.MEANING % meaning

        print(message)

def show_word_usage_example(example, highlight, leading_whitespaces=0):
    if example:
        message = leading_whitespaces * ' ' + Messages.SEE_EXAMPLE % example

        if highlight:
            message = highlighter.highlight_with_to(message)

        print(message)

def show_statistics(stats):
    print('+ %d last' % stats["last"])

def show_forgotten_words(forgotten_words):
    print(Messages.FORGOTEEN_WORDS % ', '.join(forgotten_words))

def show_game_started_message():
    log(Messages.GAME_STARTED)

def show_game_over_message():
    log(Messages.GAME_OVER)
