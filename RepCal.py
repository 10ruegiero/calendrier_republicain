#!/usr/bin/python

# Programme donnant une date dans le calendrier républicain en fonction de sa date dans le calendrier grégorien

# Import des modules time et datetime
import time
import datetime
from daterepclass import daterepublicaine


# Fonction calculant le nombre de jours entre une date donnée et le 22 septembre 1792, soit le 1er Vendémiaire de l'an I
def nbr_jours_depuis_le_22_septembre_1792(date_greg):
    date_cible = datetime.date(date_greg.tm_year,date_greg.tm_mon,date_greg.tm_mday)
    vingtdeux_septembre_1792 = datetime.date(1792,9,22)
    nbr_jours = date_cible - vingtdeux_septembre_1792
    return nbr_jours

# Fonction déroulant le calendrier républicain depuis le 1er Vendémiaire de l'an I, en fonction du nombre de jours demandés
def date_republicaine_depuis_lan_I(jours):



    # Création d'un objet date républicaine
    date_rep = daterepublicaine(1,1,1)

    jours_ecoulees = 0
    while jours_ecoulees < jours:
        jours_ecoulees += 1

        if date_rep.month < 13:
            if date_rep.day == 30:
                date_rep.day = 0
                date_rep.month +=1
        if date_rep.month == 13:
            if date_rep.est_bissextile():
                if date_rep.day == 6 :
                    date_rep.day = 0
                    date_rep.month = 1
                    date_rep.year +=1
            else:
                if date_rep.day == 5 :
                    date_rep.day = 0
                    date_rep.month = 1
                    date_rep.year += 1
        date_rep.day += 1

    return date_rep

# Fonction Main
def main():
    # Saisie utilisateur
    #date_saisie = time.strptime(input("Veuillez saisir une date au format jj/mm/aaaa:"),"%d/%m/%Y")

    # Debug input
    date_saisie = time.strptime("28/07/2018","%d/%m/%Y")
    # date_saisie = time.strptime("22/09/1792","%d/%m/%Y")
    # date_saisie = time.strptime("24/11/1793","%d/%m/%Y")



    # Calcul du nombre de jour depuis le 22 septembre 1792
    jours_depuis_le_1er_vendemiaire = nbr_jours_depuis_le_22_septembre_1792(date_saisie)

    # Parcours fictif du calendrier républicain
    date_rep = date_republicaine_depuis_lan_I(jours_depuis_le_1er_vendemiaire.days)

    #Sortie console
    print(date_rep)

if __name__== "__main__":
  main()