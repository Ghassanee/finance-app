
import BVCscrap as load
import pandas as pd

class actif:

    def __init__(self, actif_name: str):
        self.actif_name = actif_name

    def get_data(self, date_debut, date_end):
        return load.loadata(self.actif_name, start=date_debut, end=date_end)

    def get_intraday(self):
        # Intraday
        return load.getIntraday(self.actif_name)

    def get_donnees_seance(self):

        # Données de la Scéance

        print('Capitalisation : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Capitalisation']))
        print('Cours : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Cours']))
        print('Cours de Cloture de la Veille  : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Cours de cloture veille']))
        print('Devise de Cotation : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Devise de cotation']))
        print('Nombre de Titres : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Nombre de titres']))
        print('Ouverture : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Ouverture']))
        print('Plus BAS : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Plus bas']))
        print('Plus HAUT : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Plus haut']))
        print('Variation : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Variation']))
        print('Volume : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Volume']))
        print('Volume en Titres : {}  \n'.format(load.getCours(
            self.actif_name)['Données_Seance']['Volume en titres']))

    def get_meilleur_limite(self):

        # Meilleur Limite

        print('Prix Achat : {}  '.format(load.getCours(
            self.actif_name)['Meilleur_limit']['Prix achat']))
        print('Quantité Achat : {}  \n'.format(load.getCours(
            self.actif_name)['Meilleur_limit']['Quantite_achat']))
        print('Prix Vente : {}  '.format(load.getCours(
            self.actif_name)['Meilleur_limit']['Prix de vente']))
        print('Quantité Vente : {}  \n'.format(load.getCours(
            self.actif_name)['Meilleur_limit']['Quantite_vente']))

    def get_donnees_sean_prec(self):

        # Données De La Scéance Précédante

        return pd.DataFrame(load.getCours(self.actif_name)['Seance_prec'])

    def get_dernieres_transac(self):

        # Dernière Transaction

        return pd.DataFrame(load.getCours(self.actif_name)['Dernieres_Tansaction'])

    def get_info_societe(self):

        # Informations Complémentaire

        print('Commissaire Aux Comptes : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Commissaire_aux_comptes']))
        print('Date de Constitution : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Date_de_constitution']))
        print('Date Introduction : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Date_introduction']))
        print('Durée Exercice Social : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Durée_Exercice_Social']))
        print('ISIN : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['ISIN']))
        print('Objet_social : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Objet_social']))
        print('Raison_sociale : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Raison_sociale']))
        print('Secteur_activité : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Secteur_activité']))
        print('Siege_social : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Siege_social']))
        print('Ticker : {} \n '.format(load.getKeyIndicators(
            self.actif_name)['Info_Societe']['Ticker']))

    def Actionnaires(self):

        # Actionnaires

        r = load.getKeyIndicators(self.actif_name)['Actionnaires']
        z = list(load.getKeyIndicators(self.actif_name)['Actionnaires'].keys())
        for i in range(0, len(z)):
            print('{} : {} %'.format(z[i], r[z[i]]))

    def Get_Ratio(self):

        # Ratios

        return pd.DataFrame(load.getKeyIndicators(self.actif_name)['Ratio'])

    def resume_index(self):

        # Resumé Des Indices

        return pd.DataFrame(load.getIndex()['Resume indice']).T

    def get_div(self):

        # Dividende de l'actif

        return pd.DataFrame(load.getDividend(self.actif_name))

    def get_pond(self):

        # Ponderations

        return pd.DataFrame(load.getPond())

    def recap_indice(self):

        # Récapitulation Des Indices

        return pd.DataFrame(load.getIndexRecap()['Indice'])

    def recap_volume(self):

        # Récapitulation volume

        return load.getIndexRecap()['Volume Global']

    def recap_Plus_Forte_Hausse(self):

        # Plus Forte Hausse De L'Actif

        return load.getIndexRecap()['Plus forte hausse']

    def recap_Plus_Forte_Baisse(self):

        # Plus Forte Baisse de l'Actif

        return load.getIndexRecap()['Plus forte baisse']

    def get_fourchette_affichee(self):

        # Fourchette Affichée

        return float(load.getCours(self.actif_name)['Meilleur_limit']['Prix de vente'])-float(load.getCours(self.actif_name)['Meilleur_limit']['Prix achat'])

    def get_prix_moy(self):

        # Prix Moyen de Marché

        return (float(load.getCours(self.actif_name)['Meilleur_limit']['Prix de vente'])+float(load.getCours(self.actif_name)['Meilleur_limit']['Prix achat']))/2

    def get_fourchette_relat(self):

        # Fourchette Relative

        return self.get_fourchette_affichee()/self.get_prix_moy()

    def get_fourchette_effect(self):

        # Fourchette Effective

        pt = float(input('Prix de réel de Transaction ?'))
        return pt-self.get_prix_moy()

    def get_fourchette_effect_relat(self):

        # Fourchette Effective Relative

        return self.get_fourchette_effect()/self.get_prix_moy()

    def get_corwin(self):

        # Corwin Indicator

        return (float(load.getCours(self.actif_name)['Données_Seance']['Plus haut'])-float(load.getCours(self.actif_name)['Données_Seance']['Plus bas']))/float(load.getCours(self.actif_name)['Données_Seance']['Plus haut'])

    def get_Quant_moy(self, date_deb, date_fin):
        # Volume Moyen de Transaction
        return (self.get_data(date_deb, date_fin)['Volume']*self.get_data(date_deb, date_fin)['Value']).mean()

    def LIX(self, date_deb, date_fin):

        # LIX Indicator

        import numpy as np
        return ((np.log((self.get_data(date_deb, date_fin)['Volume']*self.get_data(date_deb, date_fin)['Value']*self.get_data(date_deb, date_fin)['Value'])/(self.get_data(date_deb, date_fin)['High']-self.get_data(date_deb, date_fin)['Low'])))).min()

    def get_indice_sect(self):

        # Indice sectorielle

        return load.getIndex()['Indices sectoriels']

    def get_indice_rentab(self):

        # Indice De Rentabilité

        return load.getIndex()['Indice rentabilite']
