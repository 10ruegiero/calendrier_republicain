#!/usr/bin/python
# Import des modules time et datetime
import datetime

# Définition d'un objet date républicaine
class daterepublicaine(datetime.date):
    # Liste des 12 mois républicains
    # (13 mois avec les Sansculottides, 5 jours additionnels en fin d'année, 6 les années bisexxtiles)
    mois_rep = ["Vendémiaire", "Brumaire", "Frimaire", "Nivôse", "Pluviôse", "Ventôse", "Germinal", "Floréal",
                "Prairial", "Messidor", "Thermidor", "Fructidor", "Sanculottides"]

    def __init__(self,year,month,day):
        self.replace(year,month,day)

    def __str__(self):
        date_text = "%i %s de l'an %i" % (self.day, mois_rep[self.month - 1], date_republicaine[2])
        return date_text

    def suis_bissextile(self):
        if (self.year % 4 == 3 and self.year % 100 != 3) or self.year % 400 == 3:
            return True
        else:
            return False

    def est_bissextile(year):
        if (year % 4 == 3 and year % 100 != 3) or year % 400 == 3:
            return True
        else:
            return False