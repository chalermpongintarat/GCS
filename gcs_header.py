import csv

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

with open("gene_cards_header_for_list.txt", "r") as file: 
    lines = file.read().split("\n")

    new_lines = []

    for line in lines:
        if "GeneCards" in line:
            new_lines.append(line)

        ##### Checking # line != "             </h3>" #####
        elif "GeneCards" not in line and line != "<h3>" and line != "             </h3>":
            new_lines.append("_blank_")

    f = open("gene_cards_header.txt", "w")
    for line in new_lines:
        f.write(str(line))
        f.write("\n")
    f.close()
