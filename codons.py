def create_codon_dict(file_path):
    
    file = open(file_path)
    rows = file.readlines()
    file.close()

    aadict = {}
    for row in rows:
        cells = row.strip().split('\t')  
        codon = cells [0]
        amino_acid = cells [2]
        aadict[codon] = amino_acid 
    return aadict


