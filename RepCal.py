#!/usr/bin/python

# Programme donnant une date dans le calendrier républicain en fonction de sa date dans le calendrier grégorien

# Import des modules time et datetime
import time
import datetime
from daterepclass import daterepublicaine




# Fonction déroulant le calendrier républicain depuis le 1er Vendémiaire de l'an I, en fonction du nombre de jours demandés
def date_republicaine(date_greg):
    date_cible = datetime.date(date_greg.tm_year, date_greg.tm_mon, date_greg.tm_mday)
    vingtdeux_septembre_1792 = datetime.date(1792, 9, 22)
    nbr_jours = date_cible - vingtdeux_septembre_1792

    jours_ecoulees = 0
    r_year = 1
    r_month = 1
    r_day = 1

    # Parcours du calendrier républicain
    while jours_ecoulees < nbr_jours.days:
        jours_ecoulees += 1

        if r_month < 13:
            if r_day == 30:
                r_day = 0
                r_month +=1
        if r_month == 13:
            if daterepublicaine.est_bissextile(r_year):
                if r_day == 6 :
                    r_day = 0
                    r_month = 1
                    r_year +=1
            else:
                if r_day == 5 :
                    r_day = 0
                    r_month = 1
                    r_year += 1
        r_day += 1

    # Création d'un objet date républicaine
    date_rep = daterepublicaine(r_year,r_month,r_day)
    return date_rep

# Fonction Main
def main():
    # Saisie utilisateur
    #date_saisie = time.strptime(input("Veuillez saisir une date au format jj/mm/aaaa:"),"%d/%m/%Y")

    # Debug input
    date_saisie = time.strptime("28/07/2018","%d/%m/%Y")
    # date_saisie = time.strptime("22/09/1792","%d/%m/%Y")
    # date_saisie = time.strptime("24/11/1793","%d/%m/%Y")

    # Conversion de la date grégorienne en date républicaine
    date_rep = date_republicaine(date_saisie)

    #Sortie console
    print(date_rep)

if __name__== "__main__":
  main()