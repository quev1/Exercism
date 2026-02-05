def to_rna(dna_strand):
    
    dna_to_rna_dict = {"A":"U", "T":"A", "C":"G", "G":"C"}
    
    rna_sequence = ""
    
    for nucleotide in dna_strand:
        rna_sequence += dna_to_rna_dict[nucleotide]

    return rna_sequence
                    
