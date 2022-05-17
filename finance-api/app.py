from flask import Flask, request
import BVCscrap as load
import numpy as np
import pandas as pd
from sqlalchemy import JSON
from flask_jsonpify import jsonpify
from flask_cors import CORS

load.getIntraday('CIH')
load.notation()


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


def get_info(actif_name, option):
    dd = actif(actif_name)
    cours = load.getCours(actif_name)

    if option in ['Données_Seance', 'Meilleur_limit', 'Dernieres_Tansaction', 'Seance_prec']:
        print(pd.DataFrame(cours[option]))
        print('ssss')
        return pd.DataFrame(cours[option])

    elif option in ['Info_Societe', 'Actionnaires', 'Chiffres_cles', 'Ratio']:
        indicateur = load.getKeyIndicators(actif_name)
	    # indicateur.keys()
        return pd.DataFrame(indicateur[option])
    elif option == "Intraday":
        return dd.get_intraday()


def get_indice(option):

    if option in ['Resume indice', 'Indice rentabilite', 'Indices en devises', 'Indice FTSE', ]:
        index = load.getIndex()
        index.keys()
        index[option]
        return pd.DataFrame(index[option])

    elif option in ['Indice', 'Volume Global', 'Plus forte hausse', 'Plus forte baisse']:
        recap = load.getIndexRecap()
        recap.keys()
        recap[option]
        return pd.DataFrame(recap[option])
    elif option == "poids":
        return pd.DataFrame(load.getPond())


def get_indicator_de_liquidity(actif_name, option, pt, date_deb, date_fin):
    dd = actif(actif_name)

    if option == 'Fourchette affichee':
        return float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])-float(load.getCours(actif_name)['Meilleur_limit']['Prix achat'])
    elif option == 'Prix moyen':
        return (float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])+float(load.getCours(actif_name)['Meilleur_limit']['Prix achat']))/2
    elif option == 'Fourchette relative':
        return (float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])-float(load.getCours(actif_name)['Meilleur_limit']['Prix achat']))/((float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])+float(load.getCours(actif_name)['Meilleur_limit']['Prix achat']))/2)
    elif option == 'Fourchette effective':
        return pt-(float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])+float(load.getCours(actif_name)['Meilleur_limit']['Prix achat']))/2
    elif option == "Fourchette effective relative":
        return (pt-(float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])+float(load.getCours(actif_name)['Meilleur_limit']['Prix achat']))/2) / ((float(load.getCours(actif_name)['Meilleur_limit']['Prix de vente'])+float(load.getCours(actif_name)['Meilleur_limit']['Prix achat']))/2)
    elif option == "Corwin":
        return (float(load.getCours(actif_name)['Données_Seance']['Plus haut'])-float(load.getCours(actif_name)['Données_Seance']['Plus bas']))/float(load.getCours(actif_name)['Données_Seance']['Plus haut'])
    elif option == "Quant_moy":
        return (dd.get_data(date_deb, date_fin)['Volume']*dd.get_data(date_deb, date_fin)['Value']).mean()
    elif option == "LIX":
        return ((np.log((dd.get_data(date_deb, date_fin)['Volume']*dd.get_data(date_deb, date_fin)['Value']*dd.get_data(date_deb, date_fin)['Value'])/(dd.get_data(date_deb, date_fin)['High']-dd.get_data(date_deb, date_fin)['Low'])))).min()


app = Flask(__name__)

CORS(app)

cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/info')
def info():
    actif = request.args.get('actif')
    option = request.args.get('option')
    # df_list = get_info(actif, option).values.tolist()
    # df_list_keys = get_info(actif, option).keys()
    # JSONP_data = jsonpify(df_list)
    # jsonKeys = jsonpify(df_list_keys)
    return get_info(actif, option).to_json()


@app.route('/indice')
def indice():
    indice = request.args.get('indice')
    print(indice)

    return get_indice(indice).to_json()


@app.route('/indicator_de_liquidity', methods=['POST', 'GET'])
def indicator_de_liquidity():
    actif_name = request.args.get('actif_name')
    option = request.args.get('option')
    pt = request.args.get('pt')
    date_deb = request.args.get('date_deb')
    date_fin = request.args.get('date_fin')
    print(date_deb)
    return get_indicator_de_liquidity(actif_name, option, pt, date_deb, date_fin).to_json()
