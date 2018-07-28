#!/usr/bin/python

# Programme donnant une date dans le calendrier républicain en fonction de sa date dans le calendrier grégorien

# Import des modules time et datetime
import time
import datetime


"""
L'année Républcaine

L'année du calendrier républicain était découpée en douze mois de trente jours chacun (soit 360 jours)
# Plus cinq jours complémentaires les années communes ou six les années sextiles
Elle débute le 1er vendémiaire an I (22 septembre 1792),


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


"""Liste des mois grégoriens et républicains"""
mois_gregor = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

mois_rep = ["Vendémiaire","Brumaire","Frimaire","Nivôse","Pluviôse","Ventôse","Germinal","Floréal","Prairial","Messidor","Thermidor","Fructidor","Sanculottides"]


# Fonction calculant le nombre de jours entre une date donnée et le 22 septembre 1792, soit le 1er Vendémiaire de l'an I
def nbr_jours_depuis_le_22_septembre_1792(date_greg):
    date_cible = datetime.date(date_greg.tm_year,date_greg.tm_mon,date_greg.tm_mday)
    vingtdeux_septembre_1792 = datetime.date(1792,9,22)
    nbr_jours = date_cible - vingtdeux_septembre_1792
    return nbr_jours

# Fonction testant la bissextilité
def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        return True
    else:
        return False

# Fonction testant la bissextilité d'une année républicaine
def rep_est_bissextile(annee):
    if (annee % 4 == 3 and annee % 100 != 3) or annee % 400 == 3:
        return True
    else:
        return False

# Fonction déroulant le calendrier républicain depuis le 1er Vendémiaire de l'an I, en fonction du nombre de jours demandés
def date_republicaine_depuis_lan_I(jours):
    # Le calendrier commence le 1er Vendémiaire de l'an I
    decade = 0
    r_jour = 1
    r_mois = 1
    r_annee = 1

    jours_ecoulees = 0

    while jours_ecoulees < jours:
        jours_ecoulees += 1

        if r_mois < 13:
            if r_jour == 30:
                r_jour = 0
                r_mois +=1
        if r_mois == 13:
            if rep_est_bissextile(r_annee):
                if r_jour == 6 :
                    r_jour = 0
                    r_mois = 1
                    r_annee +=1
            else:
                if r_jour == 5 :
                    r_jour = 0
                    r_mois = 1
                    r_annee += 1

        r_jour += 1

    date_republicaine = [r_jour,r_mois,r_annee]
    return date_republicaine

# Fonction transformation un date_republicaine sous format string
def format_date_republicaine(date_republicaine):
    date_text = "%i %s de l'an %i" % (date_republicaine[0],mois_rep[date_republicaine[1]-1],date_republicaine[2])
    return date_text

# Fonction Main
def main():
    # Saisie utilisateur
    date_saisie = time.strptime(input("Veuillez saisir une date au format jj/mm/aaaa:"),"%d/%m/%Y")

    # Debug input
    # date_saisie = time.strptime("28/07/2018","%d/%m/%Y")
    # date_saisie = time.strptime("22/09/1792","%d/%m/%Y")
    # date_saisie = time.strptime("24/11/1793","%d/%m/%Y")



    # Calcul du nombre de jour depuis le 22 septembre 1792
    jours_depuis_le_1er_vendemiaire = nbr_jours_depuis_le_22_septembre_1792(date_saisie)

    # Parcours fictif du calendrier républicain
    date_rep = date_republicaine_depuis_lan_I(jours_depuis_le_1er_vendemiaire.days)

    # Formatage de la date en texte
    date_rep = format_date_republicaine(date_rep)

    #Sortie console
    print(date_rep)

if __name__== "__main__":
  main()