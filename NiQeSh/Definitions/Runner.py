#!/usr/bin/python3
from . import Errors
from . import Printing
from . import Files


def run_from_file(file_name, level=0):
    if run_level(file_name, "check", level):
        print(file_name + ": Your code seems good. I am starting executing it.")
        if level == 0:
            Files.refresh_folder()
        if run_level(file_name, "execute", level):
            print(file_name + ": Your code was executed.")
            return True
    return False


def run_level(file_name, mode, level):
    args = [False, True, 0, 1, -1]
    #   Arguments:
    #   [End, NoError, TypeOfExecutedLine, Line, MomentOfCode]
    #   Results:
    #   [Things, LocationNames, LocationStates, Actions]
    [[things, locations, states, actions], success] = run_file(file_name, args)
    if success:
        actions = rewrite_actions(actions)
        availability = check_if_available(actions)
        if mode == "execute":
            script_file_name = "NiQeM-result/Mantle/Level-" + str(level) + ".js"
            Files.initial_creating(level)
            Printing.print_new_html(level)
            Printing.print_vars(script_file_name, things, level)
            Printing.print_locations(script_file_name, locations, availability)
            Printing.print_states(script_file_name, states)
            Printing.print_actions(script_file_name, actions)
        return True
    else:
        if mode == "execute":
            Files.refresh_folder()
        return False


def run_file(file_name, args):
    results = ["", [], [], []]
    read_file = open(file_name, "r")
    for line in read_file:
        [args, results] = read_line(line, args, results)
        if not args[1]:
            read_file.close()
            return [[], False]
        elif args[0]:
            read_file.close()
            return [results, True]
        else:
            args[3] += 1


def read_line(line, args, results):
    if line in ["\n", " \n"]:
        return [args, results]
    line = line.replace("\n", "")
    if args[2] == 0:
        if line != "{":
            Errors.level_start_error(line, args[3])
            args[1] = False
            return [args, []]
        args[2] = 1
    elif args[2] == 1:
        tabs = num_of_tabs(line)
        if tabs == -1:
            Errors.wrong_count_of_spaces_error(line, args[3])
            args[1] = False
            return [args, []]
        elif tabs != 1:
            Errors.things_choosing_error(line, args[3])
            args[1] = False
            return [args, []]
        line = remove_tabs(line, tabs)
        results[0] = line
        args[2] = 2
    else:
        tabs = num_of_tabs(line)
        if tabs == -1:
            Errors.wrong_count_of_spaces_error(line, args[3])
            args[1] = False
            return [args, []]
        elif tabs == 1:
            line = remove_tabs(line, tabs)
            results[1].append(line)
            args[4] += 1
            results[2].append([])
            results[3].append([])
        elif tabs == 2:
            line = remove_tabs(line, tabs)
            results[2][args[4]].append(line)
        elif tabs == 3:
            line = remove_tabs(line, tabs)
            results[3][args[4]].append(line)
        elif line == "}":
            args[0] = True
        else:
            Errors.zero_tabs_error(line, args[3])
            args[1] = False
    return [args, results]


def num_of_tabs(line):
    tab_length = 2
    spaces = 0
    for letter in line:
        if letter == " ":
            spaces += 1
        else:
            break
    if spaces % tab_length == 0:
        return int(spaces / tab_length)
    else:
        return -1


def remove_tabs(line, tabs):
    tab_length = 2
    return line[tabs * tab_length:]


def rewrite_actions(actions):
    new_actions = []
    for place in actions:
        new_actions.append([])
        for action in place:
            action_parts = action.split("->")
            action_result = action_parts[1].split(",")
            new_actions[len(new_actions) - 1].append([action_parts[0], action_result])
    return new_actions


def check_if_available(actions):
    result = []
    for i in range(len(actions)):
        result.append(0)
    for place in actions:
        for action in place:
            for action_result in action[1]:
                if ">" in action_result:
                    result[int(action_result[1:])] = -1
    return result


def finish(level):
    Files.initial_creating(level)
    Printing.print_finish("NiQeM-result/Mantle/Level-" + str(level) + ".js")
    Printing.print_new_html(level)
    Files.clean()
