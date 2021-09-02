import csv

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

with open("gene_cards_info_for_list.txt", "r") as file: 
    lines = file.read().split("\n")

    new_lines = []

    for line in lines:
        if "_blank_" in line:
            new_lines.append(line)
        elif line == "<p>":
            new_lines.append(line)

        ##### Checking # elif "                                            " in line: #####
        elif "                                            " in line:
            line = line.replace("                                            ", "")
            new_lines.append(line)
        else:
            new_lines.append("_blank_")

    f = open("gene_cards_info_for.txt", "w")
    for line in new_lines:
        f.write(str(line))
        f.write("\n")
    f.close()

##### Next #####

with open("gene_cards_info_for.txt", "r") as file: 
    lines = file.read().split("\n")

    new_lines = []
    new_paragraph = []

    for line in lines:
        if "_blank_" in line:
            new_lines.append(line)
        elif line == "<p>":
            new_paragraph.append("<p> ")
        elif line != "<p>" and line != "_blank_" and "</p>" not in line and line != "":
            new_paragraph.append(line+" ")

        elif "</p>" in line:
            new_paragraph.append(line)
            line = ''.join(new_paragraph)
            new_lines.append(line)
            new_paragraph.clear() 

    f = open("gene_cards_info.txt", "w")
    for line in new_lines:
        f.write(str(line))
        f.write("\n")
    f.close()
    