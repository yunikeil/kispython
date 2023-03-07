import os
import re


filename = r"data\levels\game.md"
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, filename)


data = []

def 
with open(file_path, "r", encoding="utf-8") as file:
    data = file.read().replace("\n\n", "\n")
    block_names = re.findall(r"(\#\#\s\[.*?\]\(\#+[0-9]*\))", data)
    for line in data.split('\n'):
        block_indexes










