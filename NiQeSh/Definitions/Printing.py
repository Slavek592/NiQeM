#!/usr/bin/python3


def print_vars(file_name, things, level):
    file = open(file_name, "a")
    file.write(
        "var level = " + str(level) + ";\n"
        "var things = " + str(things) + ";\n"
        "var thing = 0;\n"
        "var place = 0;\n"
    )


def print_locations(file_name, locations, availability):
    file = open(file_name, "a")
    file.write(
        "var places = " + str(locations) + ";\n"
        "var solved = " + str(availability) + ";\n"
    )


def print_states(file_name, location_states):
    file = open(file_name, "a")
    file.write(
        "var place_states = " + str(location_states) + ";\n"
    )


def print_actions(file_name, actions):
    file = open(file_name, "a")
    file.write(
        "function Use()\n"
        "{\n"
        "    document.getElementById(\"comment\").innerHTML = \"\";\n"
        "    if (false)\n"
        "    {}\n"
    )
    for place in range(len(actions)):
        for action in range(len(actions[place])):
            file.write(
                "    else if (place == " + str(place) + " && things[thing] == " + actions[place][action][0]
                + " && solved[" + str(place) + "] == " + str(action) + ")\n"
                "    {\n"
                "        solved[" + str(place) + "] = " + str(action + 1) + ";\n"
                "        SetAppearance()\n"
            )
            for result in actions[place][action][1]:
                if "+" in result:
                    file.write(
                        "        things.push(" + result.replace("+", "") + ");\n"
                    )
                elif ">" in result:
                    file.write(
                        "        solved[" + result.replace(">", "") + "] = 0;\n"
                    )
                elif "*" in result:
                    file.write(
                        "        UnlockNextLevel()\n"
                    )
            file.write(
                "    }\n"
            )
    file.write(
        "    else\n"
        "    {\n"
        "        document.getElementById(\"comment\").innerHTML = \"You can not use this there.\";\n"
        "    }\n"
        "}\n"
    )


def print_new_html(level):
    read_file = open("NiQeM-result/Quest.html", "r")
    write_file = open("NiQeM-result/Level-" + str(level) + ".html", "w")
    line_number = 0
    for line in read_file:
        if line_number == 6:
            write_file.write("        <script src=\"Mantle/Level-" + str(level) + ".js\"></script>\n")
        elif line_number == 10:
            write_file.write("        <h1 id=\"heading\">Level " + str(level) + "</h1>\n")
        write_file.write(line)
        line_number += 1


def print_finish(file_name):
    file = open(file_name, "a")
    file.write(
        "var things = [''];\n"
        "var thing = 0;\n"
        "var place = 0;\n"
        "var places = ['Congrats, You have won!'];\n"
        "var solved = [0];\n"
        "function Use()\n"
        "{}\n"
    )
