import output
import os

class Game:
    def __init__(self, options):
        repo = options["repository"]

        self.repo = repo
        self.list = sorted(repo.get_words(), key=str.lower)
        self.answered = []

        self.highlight = "highlight" in options and options["highlight"]

        self.show_examples = "examples" in options and options["examples"]

        self.show_meanings = "meanings" in options and options["meanings"]

    def start_game(self):
        output.show_game_started_message()

    def exit_game(self):
        output.show_forgotten_words(self.list)
        output.show_game_over_message()
        exit()

    def show_help(self):
        output.show_answered(self.answered)

    def congratulation(self):
        output.show_congratulation()

    def play(self):
        self.start_game()

        while self.list:
            line = input('> ').strip().lower()
            self.handle_next(line)
            print()

        self.congratulation()

    def handle_right(self, word):
        self.list.remove(word)
        self.answered.append(word)

        self.show_info(word)

        output.show_statistics({"last":len(self.list)})

    def show_info(self, word):
        info = self.repo.get_info(word)

        if "link" in info:
            print(info["link"])

        if self.show_examples and "examples" in info:
            output.show_word_usage_examples(info["examples"], self.highlight)

        if self.show_meanings and "meanings" in info:
            output.show_word_meanings(info["meanings"])

    def handle_wrong(self, word):
        print('-')

    def handle_next(self, line):
        if line == '-':
            self.exit_game()

        if line == '?':
            self.show_help()
            return

        if line in self.list:
            self.handle_right(line)
        else:
            self.handle_wrong(line)

def get_game(options):
    return Game(options)
