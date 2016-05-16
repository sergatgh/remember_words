from os import listdir

class WordsSourse:

    def __init__(self, start_path):
        self.path = start_path
        self.files = sorted(listdir(start_path), key = lambda str: (len(str), str.lower()))

    def get_from_interactive(self):
        files = self.files

        if len(files) == 1:
            return [self.path + files[0]]

        print("\n\033[1mSELECT ONE OF THE FILES BELOW:\033[0m\n")

        for i, f in enumerate(files):
            print('{num}) {file}\n'.format(num = i + 1, file = f))

        while True:
            num_str = input('Enter the number of the file: ')

            inp = self.handle_files_input(num_str)

            if inp:
                return inp

    def handle_files_input(self, nums):
        numbers = nums.split()
        result = []

        for number in numbers:
            if number.isnumeric() and self.file_exists(int(number) - 1):
                handled = self.handle_file_input(int(number) - 1)
                result.append(handled)
            else:
                print("Sorry, {num} not found".format(num = number))
                return False

        return result

    def file_exists(self, num_in_array):
        return num_in_array in range(len(self.files))

    def handle_file_input(self, num_in_array):
        return self.path + self.files[num_in_array]

def get_files(directory):
    return WordsSourse(directory).get_from_interactive()