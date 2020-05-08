big_data = """Le sénateur, dont il a été parlé plus haut, était un homme entendu qui 
    avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font 
    obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à 
    son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt. 
    C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant 
    tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à 
    des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes 
    aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré 
    pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun.
    [...]
    (Les Misérables, Victor Hugo)
    """

import re

def is_part_of_a_word(character):
    return len(re.findall('\w', character, flags = re.UNICODE))  

def get_words(text):
    print("Je commence à lire le texte maintenant")
    
    words = []
    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":
                words += [current_word]
                current_word = ""
        else:
            current_word += character
    return words


def filter_by_size(words):
    return [w for w in words if len(w) >= 6]

def filter_by_letters(words):
    return [w for w in words if "a" in w]
            

words = get_words(big_data)
print("Nombre de mots: %i" % len(words))
words = filter_by_size(words)
print("Nombre de mots: %i" % len(words))
words = filter_by_letters(words)
print("Nombre de mots: %i" % len(words))
        
print(words)