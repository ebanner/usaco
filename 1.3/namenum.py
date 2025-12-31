"""
ID: edward.10
LANG: PYTHON3
TASK: namenum
"""


def get_serial_number():
    with open('namenum.in', 'r') as f:
        serial_number = f.readline().strip()
        return serial_number


def get_dictionary():
    with open('dict.txt', 'r') as f:
        words = [line.strip() for line in f.readlines()]
        return set(words)


def get_letters(number):
    return {
        2: list('ABC'), 5: list('JKL'), 8: list('TUV'),
        3: list('DEF'), 6: list('MNO'), 9: list('WXY'),
        4: list('GHI'), 7: list('PRS'),
    }[int(number)]


def get_possible_words(serial_number, dictionary):
    def dfs(nums, word=''):
        if not nums:
            return [word] if word in dictionary else []

        number, rest = nums[0], nums[1:]
        letters = get_letters(number)
        possible_words = []
        for letter in letters:
            possible_words += dfs(rest, word+letter)

        return possible_words

    possible_words = dfs(serial_number)
    return possible_words


if __name__ == '__main__':
    serial_number = get_serial_number()
    dictionary = get_dictionary()

    possible_words = get_possible_words(serial_number, dictionary)
    with open('namenum.out', 'w') as f:
        if possible_words:
            for possible_word in sorted(possible_words):
                f.write(possible_word + '\n')
        else:
            f.write('NONE' + '\n')

