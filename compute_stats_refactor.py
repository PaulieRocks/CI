import statistics

def read_ints(file):
    """ reads the integers from a file passed as input
    input: a file in .txt format with integers seperated by newline
    output: list of integers as present in the file"""
    values = []
    with open(file, "r") as f:
        for line in f:
            values.append(int(line))
    return values


def compute_count(file):
    """
    The function computes the number of values present in the file
    :param file: a newline seperated integer file
    :return: an integer representing the count
    """
    return len(read_ints(file))


def compute_sum(file):
    """
    The function computes the sum of all the numbers present in the file
    :param file: a newline seperated integer file
    :return: an integer representing the sum
    """

    sum = 0
    for i in read_ints(file):
        sum += i
    return sum


def compute_average(file):
    """
    The function computes the average of all the numbers present in the file
    :param file: a newline seperated integer file
    :return: a number representing the average
    """

    return compute_sum(file) / compute_count(file)


def compute_minimum(file):
    return min(read_ints(file))


def compute_maximum(file):
    return max(read_ints(file))

def compute_harmonic_mean(list_ints):
    return statistics.harmonic_mean(list_ints)


if __name__ == '__main__':
    print(read_ints('random_nums.txt'))
    print(compute_count('random_nums.txt'))
    print(compute_sum('random_nums.txt'))
    print(compute_average('random_nums.txt'))
    print(compute_minimum('random_nums.txt'))
    print(compute_maximum('random_nums.txt'))
