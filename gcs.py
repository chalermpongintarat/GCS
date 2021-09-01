import csv

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# gene_cards_header = []
# gene_cards_info = []
gene_cards_summary_for = []
with open("gene_list.txt", "r") as file: 
    line = file.read().split("\n")
    for gene_symbol in line:
        None
        # print(gene_symbol)

        url = "https://www.genecards.org/cgi-bin/carddisp.pl?gene="+gene_symbol

        response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        url_open = urlopen(response).read()
        html_page = url_open.decode('utf-8')

        soup = BeautifulSoup(html_page, 'html.parser')
        soup.prettify()

        gc_subsection_header = soup.find_all('div', attrs={'class':'gc-subsection-header'})
        gene_cards_header = []
        for h3 in gc_subsection_header:
            header = h3.find_all('h3')
            gene_cards_header.append(header)

        # str_gene_cards_header = str(gene_cards_header[2][0])
        str_gene_cards_header = str(gene_cards_header[0])

        # print(str_gene_cards_header)

        gc_subsection = soup.find_all('div', attrs={'class':'gc-subsection'})
        gene_cards_info = []
        for h3 in gc_subsection:
            info = h3.find_all('p')
            gene_cards_info.append(info)

        # str_gene_cards_info = str(gene_cards_info[7][0])
        str_gene_cards_info = str(gene_cards_info[7])

        # print(str_gene_cards_info)

        # gene_cards_summary_for = []
        # gene_cards_summary_for.append(str_gene_cards_header)
        gene_cards_summary_for.append(str_gene_cards_info)

        # csv_col = [[gene_cards_summary_for]]
        # f = open('csv_gene_cards_summary_for.csv', 'w')
        # with f:
        #     writer = csv.writer(f)
        #     for row in csv_col:
        #         writer.writerow(row)

# print(gene_cards_summary_for)

f = open("gene_cards_info_for_402_500.txt", "w")
f.writelines(str(gene_cards_summary_for))
f.close()
