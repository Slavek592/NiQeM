#!/usr/bin/python3
import os
import zipfile
import shutil


def refresh_folder():
    shutil.rmtree("NiQeM-result")
    with zipfile.ZipFile("Template.zip", "r") as zip_ref:
        zip_ref.extractall("")


def initial_creating(level):
    if level == 0:
        os.mkdir("NiQeM-result/Mantle")
    script_file = open("NiQeM-result/Mantle/Level-" + str(level) + ".js", "w")
    script_file.close()
    os.mkdir("NiQeM-result/Pictures-" + str(level))


def clean():
    os.remove("NiQeM-result/Quest.html")
