from flask import Flask, request
import BVCscrap as load
import numpy as np
import pandas as pd
from sqlalchemy import JSON
from flask_jsonpify import jsonpify
from flask_cors import CORS
import matplotlib.pyplot as plt
import plotly.express as px
import statistics as cs
from pandas.plotting import scatter_matrix
from numpy.linalg import inv
import io
import base64

load.getIntraday('CIH')
load.notation()


Attijari = pd.read_excel('Attijarii.xlsx', index_col='Séance')
Itissalat = pd.read_excel('Attissalat.xlsx', index_col='Séance')
BCP = pd.read_excel('BCP.xlsx', index_col='Séance')
Lafarge = pd.read_excel('Lafarge.xlsx', index_col='Séance')
BOA = pd.read_excel('BMCE.xlsx', index_col='Séance')
Cosumar = pd.read_excel('Cosumar.xlsx', index_col='Séance')
Ciment_Maroc = pd.read_excel('Cim_Maroc.xlsx', index_col='Séance')
Marsa_Maroc = pd.read_excel('Marsa_Marooc.xlsx', index_col='Séance')
Label_Vie = pd.read_excel('LABEL_VIE.xlsx', index_col='Séance')
Taqa_Maroc = pd.read_excel('Taqa_Maroc.xlsx', index_col='Séance')
HPS = pd.read_excel('HPS.xlsx', index_col='Séance')
Total_Maroc = pd.read_excel('Total_MAROC.xlsx', index_col='Séance')
Miniere = pd.read_excel('M_touiss.xlsx', index_col='Séance')
Mutandis = pd.read_excel('Mutandis.xlsx', index_col='Séance')
Lesieur = pd.read_excel('Lesieur.xlsx', index_col='Séance')
Addoha = pd.read_excel('Addoha.xlsx', index_col='Séance')
Atlanta = pd.read_excel('Atlanta.xlsx', index_col='Séance')
Auto_Hall = pd.read_excel('Auto_Hall.xlsx', index_col='Séance')
Snep = pd.read_excel('Snepp.xlsx', index_col='Séance')
Dar_sadaa = pd.read_excel('DAR_SADAA.xlsx', index_col='Séance')
MSI = pd.read_excel('mm.xlsx', index_col='Séance')

data_names = {'Attijari': Attijari, 'Itissalat': Itissalat, 'BCP': BCP, 'Lafarge': Lafarge, 'BOA': BOA, 'Cosumar': Cosumar, 'Ciment_Maroc': Ciment_Maroc, 'Marsa_Maroc': Marsa_Maroc, 'Label_Vie': Label_Vie, 'Taqa_Maroc': Taqa_Maroc,
              'HPS': HPS, 'Total_Maroc': Total_Maroc, 'Miniere': Miniere, 'Mutandis': Mutandis, 'Lesieur': Lesieur, 'Addoha': Addoha, 'Atlanta': Atlanta, 'Auto_Hall': Auto_Hall, 'Snep': Snep, 'Dar_Sadaa': Dar_sadaa, 'MSI': MSI}


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


def Plot_Actif_Line( actif: str):
    if actif == 'MSI':
        return data_names[actif]['Instrument'].plot(figsize=(17, 7))
    else:
        return data_names[actif]['COURS_CLOTURE'].plot(figsize=(17, 7))


def Plot_Indicateur_MA( actif: str, longueur: list):
    d = pd.DataFrame()
    d['COURS_CLOTURE'] = data_names[actif]['COURS_CLOTURE']

    for i in range(0, len(longueur)):
        d['MA : {} '.format(longueur[i])] = data_names[actif]['COURS_CLOTURE'].rolling(
            longueur[i]).mean()

    return d[list(d.columns)].plot(figsize=(17, 7))


def Plot_Indicateur_Drawdown( actif: str, tp):
    d = pd.DataFrame()

    if actif == 'MSI':
        if tp in ['max', 'max'.title(), 'max'.upper()]:
            d['cmMax'] = data_names[actif]['Instrument'].cummax()
            d['COURS_CLOTURE'] = data_names[actif]['Instrument']
            return d[['cmMax', 'COURS_CLOTURE']].plot(figsize=(17, 7))

        elif tp in ['min', 'min'.title(), 'min'.upper()]:
            d['cmMin'] = data_names[actif]['Instrument'].cummin()
            d['COURS_CLOTURE'] = data_names[actif]['Instrument']
            return d[['cmMin', 'COURS_CLOTURE']].plot(figsize=(17, 7))

    else:
        if tp in ['max', 'max'.title(), 'max'.upper()]:
            d['cmMax'] = data_names[actif]['COURS_CLOTURE'].cummax()
            d['COURS_CLOTURE'] = data_names[actif]['COURS_CLOTURE']
            return d[['cmMax', 'COURS_CLOTURE']].plot(figsize=(17, 7))

        elif tp in ['min', 'min'.title(), 'min'.upper()]:
            d['cmMin'] = data_names[actif]['COURS_CLOTURE'].cummin()
            d['COURS_CLOTURE'] = data_names[actif]['COURS_CLOTURE']
            return d[['cmMin', 'COURS_CLOTURE']].plot(figsize=(17, 7))


def Combinaison_Indicateurs( actif, cible_indicateur: list, longueur_MA=None):
    d = pd.DataFrame()
    d['COURS_CLOTURE'] = data_names[actif]['COURS_CLOTURE']

    for i in cible_indicateur:

        if i in ['max', 'max'.title(), 'max'.upper()]:
            d['cmMax'] = data_names[actif]['COURS_CLOTURE'].cummax()

        elif i in ['min', 'min'.title(), 'min'.upper()]:
            d['cmMin'] = data_names[actif]['COURS_CLOTURE'].cummin()

        elif i in ['Ma', 'ma', 'MA']:

            if longueur_MA == None:
                longueur_MA = [50]

            for i in range(0, len(longueur_MA)):
                d['MA : {} '.format(longueur_MA[i])] = data_names[actif]['COURS_CLOTURE'].rolling(
                    longueur_MA[i]).mean()

    return d[list(d.columns)].plot(figsize=(17, 7))


def Calcul_Rendement_Actifs( actif: list, tp2: str, date_debut, date_fin, tp=True):
    y = []
    for i in range(0, len(actif)):
        y.append(data_names[actif[i]])

    if tp == True:
        if tp2 == 'Quotidien':
            for i in range(0, len(y)):
                y[i]['Rendement'] = (y[i]['COURS_CLOTURE'].pct_change())

        elif tp2 == 'Cumulatif':
            for i in range(0, len(y)):
                y[i]['Rendement_Cumul'] = (
                    (y[i]['COURS_CLOTURE'].pct_change())+1).cumprod()
        return y

    elif tp == False:
        d = pd.DataFrame()

        if tp2 == 'Quotidien':
            for i in range(0, len(actif)):
                d['Rendement {}'.format(actif[i])] = (
                    data_names[actif[i]]['COURS_CLOTURE'].loc[date_debut:date_fin]).pct_change()
            return d

        elif tp2 == 'Cumulatif':
            for i in range(0, len(actif)):
                d['Rendement_Cumul {}'.format(actif[i])] = (
                    data_names[actif[i]].loc[date_debut:date_fin]['COURS_CLOTURE'].pct_change()+1).cumprod()
            return d


def Plot_Histogramme( actif):
    if actif == 'MSI':
        return (data_names[actif]['Instrument'].pct_change()).hist(
            figsize=(13, 7), bins=600)
    else:
        return (data_names[actif]['COURS_CLOTURE'].pct_change()).hist(
            figsize=(13, 7), bins=600)


def Risque_Actif( actif, date_debut, date_fin):
    ee = pd.DataFrame()
    if actif == 'MSI':
        ee['Rendement'] = data_names[actif]['Instrument'].loc[date_debut:date_fin].pct_change()
    else:
        ee['Rendement'] = data_names[actif]['COURS_CLOTURE'].loc[date_debut:date_fin].pct_change()

    return 'Risque_Actif {} : {} % '.format(actif, (ee.std()[0]*np.sqrt(252)*100))


def Covariance_Matrice( actif: list, date_debut, date_fin, plot=False):
    if plot == False:
        return Calcul_Rendement_Actifs(actif, 'Quotidien', date_debut, date_fin, False).cov()
    elif plot == True:
        from pandas.plotting import scatter_matrix
        scatter_matrix(Calcul_Rendement_Actifs(actif, 'Quotidien', date_debut,
                       date_fin, False), hist_kwds={'bins': 600}, alpha=0.8, figsize=(17, 9))
        plt.show()


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
    return get_indicator_de_liquidity(actif_name, option, pt, date_deb, date_fin).to_json()


@app.route('/plot_actif_line', methods=['POST', 'GET'])
def plot_actif_line():
    actif_name = request.args.get('actif_name')
    plt1 = Plot_Actif_Line(actif_name)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/plot_indicateur_ma', methods=['POST', 'GET'])
def plot_indicateur_ma():
    actif_name = request.args.get('actif_name')
    data = request.get_json()
    longueur = data.get('longueur')
    plt1 = Plot_Indicateur_MA(actif_name, longueur)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/plot_indicateur_drawdown', methods=['POST', 'GET'])
def plot_indicateur_drawdown():
    actif_name = request.args.get('actif_name')
    tp = request.args.get('tp')
    plt1 = Plot_Indicateur_Drawdown(actif_name , tp)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/combinaison_indicateurs', methods=['POST', 'GET'])
def combinaison_indicateurs():
    actif_name = request.args.get('actif_name')
    data = request.get_json()
    cible_indicateur = data.get('cible_indicateur')
    longueur_MA = data.get('longueur_MA')
    plt1 = Combinaison_Indicateurs(actif_name , cible_indicateur ,longueur_MA)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/calcul_rendement_actifs', methods=['POST', 'GET'])
def calcul_rendement_actifs():
    data = request.get_json()
    actif_name = data.get('actif')
    tp2 = data.get('tp2')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Calcul_Rendement_Actifs(actif_name ,tp2, date_debut ,date_fin)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/plot_histogramme', methods=['POST', 'GET'])
def plot_histogramme():
    actif_name = request.args.get('actif_name')
    plt1 = Plot_Histogramme(actif_name)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/risque_actif', methods=['POST', 'GET'])
def risque_actif():
    data = request.get_json()
    actif_name = data.get('actif')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Risque_Actif(actif_name , date_debut , date_fin)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()


@app.route('/covariance_matrice', methods=['POST', 'GET'])
def covariance_matrice():
    data = request.get_json()
    actif_name = data.get('actif')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Covariance_Matrice(actif_name , date_debut , date_fin)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.to_json()
