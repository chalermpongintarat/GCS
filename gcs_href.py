with open("gene.txt", "r") as file: 
    lines = file.read().split("\n")
    
    find = '<a href="/cgi-bin/carddisp.pl?gene='
    replace = '<a href="https://www.genecards.org/cgi-bin/carddisp.pl?gene='

    href = [] 
    for line in lines:
        if find in line:
            href_line = line.replace(find, replace)
        else:
            href_line = line
        href.append(href_line)

    f = open("gene_href.txt", "w")
    for line in href:
        f.write(str(line))
        f.write("\n")
    f.close()
