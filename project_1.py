#### "project_1.py"

import sys
import time

def find_largest_digit(string):
    result = None
    digit = None
    max_digit = 9
    largest_digit = -1
    for char in string:
        if char.isdigit():
           digit = int(char)
           if digit == max_digit:
              result = digit
              return result
           if digit > largest_digit:
              largest_digit = digit
    if largest_digit != -1:
       result = largest_digit
    return result

def longest_repeated_substring(string):
    length = len(string)
    substr = ''
    repeated_index = -1
    longest_repeated_substr = ''
    # get every possible repeated substring by looping through each beginning
    # character index and incrementing its ending index with each iteration
    for begin in range(length):
        for end in range(begin + 1, length):
            substr_len = end - begin
            remaining_search_len = length - end
            # if the length of the substring is greater than the remaining 
            # search length, then it is impossible for that substring and 
            # further substrings starting with the beginning character to be 
            # repeated
            if substr_len > remaining_search_len:
                break
            else:
                substr = string[begin:end]
                repeated_index = string.find(substr, end, length)
                if repeated_index != -1 and not substr.isspace():
                    if len(substr) > len(longest_repeated_substr):
                        longest_repeated_substr = substr
    if longest_repeated_substr == '':
        longest_repeated_substr = None
    return longest_repeated_substr


def main():
    if len(sys.argv) != 3:
        print('Error, must supply 2 arguments.\n\n' + 
              'Usage: python3 project_1.py <text_file> <n>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])

    entire_file = open(filename).read()
    print('\nLoaded "' + filename + '" of length ' + str(len(entire_file)))

    # take only the first n characters of entire_file
    s = entire_file[:n]
    assert(len(s) == n)
    print('n = {}\n'.format(n))

    # find the largest digit in s
    start = time.perf_counter()
    largest_digit = find_largest_digit(s)
    end = time.perf_counter()
    print('Largest digit: {}'.format(largest_digit))
    print('Elapsed time: {}\n'.format(end - start))

    # find the longest repeated substring in s
    start = time.perf_counter()
    longest_repeated_substr = longest_repeated_substring(s)
    end = time.perf_counter()
    print('Longest repeated substring: [{}]'.format(longest_repeated_substr))
    print('Elapsed time: {}\n'.format(end - start))

if __name__ == '__main__':
    main()
