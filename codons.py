def create_codon_dict(file_path):
    
    path = "/content/data/codons.txt"
    file = open(path, "r")
    rows = file.readlines()
    file.close()
    rows

    aadict = {}
    for row in rows:
        cells = row.strip().split('\t')  
        codon = cells [0]
        amino_acid = cells [2]
        aadict[codon] = amino_acid 
               
    aadict 


