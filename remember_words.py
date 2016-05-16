from sys import argv
import game
import repository
import words_input

if __name__ == '__main__':
    # List of verbs followed by a gerund
    topics_path = "./topics/"

    options = {}

    # Getting repository.
    # listname = 'verbs_followed_by_a_gerund.txt'

    # if not "--interactive-select" in argv:
    #     if len(argv) > 1 and not argv[1].startswith("--"):
    #         listname = argv[1]
    # else:
    listname = words_input.get_files(topics_path)

    options["repository"] = repository.get_repository_from_files(listname)

    # Command line options.
    # if "--highlight" in argv:
    #     options["highlight"] = True

    options["examples"] = not "--no-examples" in argv
    options["meanings"] = not "--no-meanings" in argv

    game.get_game(options).play()
