
# finds index of character within list
def index(c: chr, ls = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")): 
    if c in ls:
        return ls.index(c)
    
    return -1


alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabet_lower = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
