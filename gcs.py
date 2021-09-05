from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

with open("gene_list.txt", "r") as file: 
    line = file.read().split("\n")

    gene_cards_header_for = []
    gene_cards_info_for = []
    
    for gene_symbol in line:

        url = "https://www.genecards.org/cgi-bin/carddisp.pl?gene="+gene_symbol

        response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        url_open = urlopen(response).read()
        html_page = url_open.decode('utf-8')

        soup = BeautifulSoup(html_page, 'html.parser')
        soup.prettify()

        ##### GeneCards header #####
        gc_subsection_header = soup.find_all('div', attrs={'class':'gc-subsection-header'})
        gene_cards_header = []
        for h3 in gc_subsection_header:
            header = h3.find_all('h3')
            gene_cards_header.append(header)

        i = gene_cards_header[0][0]
        if len(i):
            gene_cards_header_for.append(i)
        else:
            gene_cards_header_for.append("_blank_")

        ##### GeneCards info #####
        gc_subsection = soup.find_all('div', attrs={'class':'gc-subsection'})
        gene_cards_info = []
        for p in gc_subsection:
            info = p.find_all('p')
            gene_cards_info.append(info)

        i = gene_cards_info[7]
        if len(i):
            gene_cards_info_for.append(i[0])
        else:
            gene_cards_info_for.append("_blank_")

    ##### GeneCards header #####
    f = open("gene_cards_header_for_list.txt", "w")
    for line in gene_cards_header_for:
        f.write(str(line))
        f.write("\n")
    f.close()

    ##### GeneCards info #####
    f = open("gene_cards_info_for_list.txt", "w")
    for line in gene_cards_info_for:
        f.write(str(line))
        f.write("\n")
    f.close()
