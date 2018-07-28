#!/usr/bin/python

# Programme donnant une date dans le calendrier républicain en fonction de sa date dans le calendrier grégorien

# Import des modules time et datetime
import time
import datetime
import  daterepublicaine


# Fonction calculant le nombre de jours entre une date donnée et le 22 septembre 1792, soit le 1er Vendémiaire de l'an I
def nbr_jours_depuis_le_22_septembre_1792(date_greg):
    date_cible = datetime.date(date_greg.tm_year,date_greg.tm_mon,date_greg.tm_mday)
    vingtdeux_septembre_1792 = datetime.date(1792,9,22)
    nbr_jours = date_cible - vingtdeux_septembre_1792
    return nbr_jours

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