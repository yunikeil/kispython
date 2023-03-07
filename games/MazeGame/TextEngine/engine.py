import os
import re


filename = r"data\levels\game.md"
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, filename)
data = ""


def split_string_with_separator(string, separator_regex):
    result = []
    for match in re.finditer(separator_regex, string):
        
    return result


with open(file_path, "r", encoding="utf-8") as file:
    data = file.read().replace("\n\n", "\n")
    data = split_string_with_separator(data, r"(\#\#\s\[.*?\]\(\#+[0-9]*\))")









