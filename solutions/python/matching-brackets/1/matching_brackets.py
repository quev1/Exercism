def is_paired(input_string):
    """
    Parcourir chaque caractère de la chaîne
    Si c’est une ouverture (, [, { → on l’ajoute à la pile
    Si c’est une fermeture ), ], } → on vérifie la dernière ouverture :
    Si la pile est vide → déséquilibré
    Si la dernière ouverture correspond → pop de la pile
    Sinon → déséquilibré
    À la fin, si la pile est vide → tout est équilibré
    """

    stack_check = []
    matching_stack = {"}":"{", ")":"(", "]":"["}
    for char in input_string:
        if char in "[({":
            stack_check.append(char)
        elif char in "])}":
            if not stack_check:
                return False
            if stack_check[-1] != matching_stack[char]:
                return False
            stack_check.pop()
    return not stack_check
            
        
