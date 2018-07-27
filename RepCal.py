#!/usr/bin/python

# Programme donnant une date dans le calendrier républicain
# en fonction de sa date dans le calendrier grégorien

# L'année du calendrier républicain était découpée en douze mois de trente jours chacun (soit 360 jours)
# Plus cinq jours complémentaires les années communes ou six les années sextiles

# Elle débute le 1er vendémiaire an I (22 septembre 1792),

"""
Les mois

    Mois d'automne (terminaison en -aire, du latin -arius, suffixe adjectival)
        Vendémiaire (22 septembre ~ 21 octobre) – Période des vendanges
        Brumaire (22 octobre ~ 20 novembre) – Période des brumes et des brouillards
        Frimaire (21 novembre ~ 20 décembre) – Période des froids (frimas)
    Mois d'hiver (terminaison en -ose à l'origine, abusivement orthographiée ôse par la suite, du latin -osus, « doté de »)
        Nivôse (21 décembre ~ 19 janvier) – Période de la neige
        Pluviôse (20 janvier ~ 18 février) – Période des pluies
        Ventôse (19 février ~ 20 mars) – Période des vents
    Mois du printemps (terminaison en -al, du latin -alis, suffixe adjectival)
        Germinal (21 mars ~ 19 avril) – Période de la germination
        Floréal (20 avril ~ 19 mai) – Période de l'épanouissement des fleurs
        Prairial (20 mai ~ 18 juin) – Période des récoltes des prairies
    Mois d'été (terminaison en -idor, du grec dôron, don)
        Messidor (19 juin ~ 18 juillet) – Période des moissons
        Thermidor (19 juillet ~ 17 août) – Période des chaleurs
        Fructidor (18 août ~ 16 septembre) – Période des fruits
"""

mois_gregor = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

mois_rep = ["Vendémiaire","Brumaire","Frimaire","Nivôse","Pluviôse","Ventôse","Germinal","Floréal","Prairial""Messidor","Thermidor","Fructidor"]


periode_mois_rep = {
    "Vendémiaire": [[22, 9], [21, 10]],
    "Brumaire": [[22, 10], [20, 11]],
    "Frimaire": [[21, 11], [20, 12]],
    "Nivôse": [[21, 12], [19, 1]],
    "Pluviôse": [[20, 1], [18, 2]],
    "Ventôse": [[19, 2], [20, 3]],
    "Germinal": [[21, 3], [19, 4]],
    "Floréal": [[20, 4], [19, 5]],
    "Prairial": [[20, 5], [18, 6]],
    "Messidor": [[19, 6], [18, 7]],
    "Thermidor": [[19, 7], [17, 8]],
    "Fructidor": [[18, 8], [21, 9]]
}


def date_republicaine_depuis_lan_I(jours):
    decade = 1
    r_mois = 1
    r_annee = 1
    date_republicaine = 1
    return date_republicaine

def date_str(date,type_de_mois):
    date_txt = str(date[0]) + " " + type_de_mois[date[1] - 1]
    return date_txt


def periode_str(periode):
    periode_txt = "Du " + date_str(periode[0]) + " au " + date_str(periode[1])
    return periode_txt
