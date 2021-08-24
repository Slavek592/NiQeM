#!/usr/bin/python3


def error_ending(line, number_of_line):
    print("I got:")
    print(line)
    print("Number of the line is:")
    print(number_of_line)


def level_start_error(line, number_of_line):
    print("Syntax error! Every level must start with the line \"{\"!")
    error_ending(line, number_of_line)


def things_choosing_error(line, number_of_line):
    print("Syntax error! Code must be followed by the line \"  ['thing', 'thing',...]\"!")
    error_ending(line, number_of_line)


def wrong_count_of_spaces_error(line, number_of_line):
    print("Syntax error! You wrote unsupported count of spaces! Spaces % tab length must be 0!")
    error_ending(line, number_of_line)


def zero_tabs_error(line, number_of_line):
    print("Syntax error! You wrote no tabs! Some are expected!")
    error_ending(line, number_of_line)
