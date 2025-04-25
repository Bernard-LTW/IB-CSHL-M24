
def translate_dna(in_protein:str)->str:
    out = "not valid"
    if in_protein == "A":
        out = "T"
    elif in_protein == "T":
        out = "A"
    elif in_protein == "C":
        out = "G"
    elif in_protein == "G":
        out = "C"

    return out


