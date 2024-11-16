import re
import time


class MNum:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return MNum(self.value * other.value)

    def __add__(self, other):
        return MNum(self.value + other.value)

    def __mul__(self, other):
        return MNum(self.value + other.value)


def solve_puzzle(filename, param=None, verbose=False):
    lines = [line.strip('\n') for line in open(filename, 'r').readlines()]

    p1 = 0
    p2 = 0

    for line in lines:
        line = re.sub(r'([0-9]+)', r'MNum(\1)', line)
        line = line.replace('*', '-')
        ans = eval(line)
        p1 += ans.value

        line = line.replace('+', '*')
        ans = eval(line)
        p2 += ans.value

    return p1, p2


def main():
    input_data_list = [
        ['sample.txt',  'sample data  ', False, False, None],
        ['data.txt',    'real data    ', True,  False, None],
    ]

    for filename, description, use_data, verbose, param in input_data_list:
        if use_data:
            start = time.time()
            p1, p2 = solve_puzzle('data/' + filename, param, verbose)
            end = time.time()
            print(p1)
            print(p2)
            print("%s \tin %d ms" % (description, round(1000 * (end - start), 2)))


if __name__ == '__main__':
    main()
