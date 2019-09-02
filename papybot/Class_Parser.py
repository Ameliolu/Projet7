class Parser:
    """classe dont les méthodes permettent de parser un texte"""
    def __init__(self):
        pass

    def supp_espaces(t):
        """
        méthode enlevant les espaces au debut et à la fin
        exemple :
        >>> Parser.supp_espaces("      le cerf    ")
        'le cerf'
        """
        t = t.strip()
        return t

    def listage(t):
        """
        méthode transformant le texte en liste
        exemple :
        >>> Parser.listage("le cerf")
        ['le', 'cerf']
        """
        t = t.split()
        return t
 
    def filtrage(liste_t, stop_words):
        """
        méthode enlevant de la liste du texte les stops words
        exemple :
        >>> Parser.filtrage(['le', 'cerf'], ['le'])
        ['cerf']
        """
        for elt in stop_words:
            for i in liste_t:
                if elt == i:
                    liste_t.remove(i)
                else:
                    pass
        return liste_t

    def final(liste_t):
        """
        méthode refaisant de la liste texte une chaîne de caractère
        exemple :
        >>> Parser.final(['cerf'])
        'cerf'
        """
        t = " ".join(liste_t)
        return t
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    STOP = ['le','la']
    choix = input("choix : ")
    texte = Parser.supp_espaces(choix)
    texte = Parser.listage(texte)
    texte = Parser.filtrage(texte, STOP)
    texte = Parser.final(texte)
    print(texte)
"""import doctest
doctest.testmod(verbose = True)"""