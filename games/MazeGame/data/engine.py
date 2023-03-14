import os
import re


filename = r"data\levels\game.md"
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, filename)


data = []


with open(file_path, "r", encoding="utf-8") as file:
    _data = file.read().replace("\n\n", "\n")
    block_names = re.findall(r"(\#\#\s\[.*?\]\(\#+[0-9]*\))", _data)
    for line in _data.split('\n'):
        if line in block_names:
            block_names.append(_data.index(line))

        










