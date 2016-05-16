import json
import os.path
import random

class BaseRepository:
    def get_words(self):
        return []

    def __iter__(self):
        return self.get_words().__iter__()

    def get_examples(self, word):
        return []

    def get_meanings(self, word):
        return []

class TextRepository(BaseRepository):
    def __init__(self, file):
        self.file_name = file

    def file_exist(self):
        return os.path.isfile(self.file_name)

    def get_words(self):
        if not self.file_exist():
            return []

        return [line.rstrip().lower() for line in open(self.file_name)]

class JsonRepository(BaseRepository):
    def __init__(self, file):
        self.file_name = file
        self.data = self.load_data()

    def file_exist(self):
        return os.path.isfile(self.file_name)

    def get_words(self):
        if not self.file_exist():
            return []

        return list(self.data.keys())

    def load_data(self):
        return json.load(open(self.file_name))

    def get_examples(self, word):
        default = []
        examples_key = "examples"
        examples = self.get_data_for_the_word(word, examples_key)

        return examples or default

    def get_meanings(self, word):
        default = []
        meanings_key = "meanings"
        meanings = self.get_data_for_the_word(word, meanings_key)

        return meanings or default

    def get_data_for_the_word(self, word, data):
        default = []
        if word not in self.data:
            return default

        if data not in self.data[word]:
            return default

        return self.data[word][data]

class RepoOfRepos(BaseRepository):

    def __init__(self, repos):
        self.repositories = repos

    def get_words(self):
        return self.get_union_result_from_method(lambda x: x.get_words())

    def get_examples(self, word):
        return self.get_union_result_from_method(lambda x: x.get_examples(word))

    def get_meanings(self, word):
        return self.get_union_result_from_method(lambda x: x.get_meanings(word))

    def get_union_result_from_method(self, method):
        result = set()
        for repo in self.repositories:
            result = set(result).union(method(repo))

        return list(result)

def get_repository_from_files(files):
    if len(files) == 1:
        return get_repository_from_file(files[0])

    return RepoOfRepos([get_repository_from_file(file) for file in files])


def get_repository_from_file(file):
    ext = os.path.splitext(file)[1]

    if ext == ".json":
        return JsonRepository(file)

    if ext == ".txt":
        return TextRepository(file)