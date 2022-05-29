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

from functions import OPCVM_CHOIX, OPCVM_FINALE, OPCVM_MAROC, Backtest, Calcul_Rendement_Actifs, Combinaison_Indicateurs, Covariance_Matrice, Monte_Carlo, Plot_Actif_Line, Plot_Front_Effic, Plot_Histogramme, Plot_Indicateur_Drawdown, Plot_Indicateur_MA, Portefeuille_Constitution, Portefeuille_Constitution_OPCVM, Portefeuille_Constitution_OPCVM_test, Portefeuille_Esper_Minimum, Portefeuille_Minim_Risk_Limite, Portefeuille_Minim_Risk_Limite_Esper, Portefeuille_Risk_Minim_Esper, Portefeuille_Risk_Minimum, Portefeuille_Tangeant, Risque_Actif, Strat, get_indicator_de_liquidity, get_indice, get_info

load.getIntraday('CIH')
load.notation()


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
    data = request.get_json()
    longueur = data.get('longueur')
    actif_name = data.get('actif_name')
    plt1 = Plot_Indicateur_MA(actif_name, longueur)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData


@app.route('/plot_indicateur_drawdown', methods=['POST', 'GET'])
def plot_indicateur_drawdown():
    actif_name = request.args.get('actif_name')
    tp = request.args.get('tp')
    plt1 = Plot_Indicateur_Drawdown(actif_name, tp)

    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData


@app.route('/combinaison_indicateurs', methods=['POST', 'GET'])
def combinaison_indicateurs():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cible_indicateur = data.get('cible_indicateur')
    longueur_MA = data.get('longueur_MA')
    plt1 = Combinaison_Indicateurs(actif_name, cible_indicateur, longueur_MA)
    my_stringIObytes = io.BytesIO()
    plt1.figure.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData


@app.route('/calcul_rendement_actifs', methods=['POST', 'GET'])
def calcul_rendement_actifs():
    data = request.get_json()
    actif_name = data.get('actif')
    tp2 = data.get('tp2')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Calcul_Rendement_Actifs(actif_name, tp2, date_debut, date_fin)
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
    print(plt1)

    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData


@app.route('/risque_actif', methods=['POST', 'GET'])
def risque_actif():
    data = request.get_json()
    actif_name = data.get('actif_name')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Risque_Actif(actif_name, date_debut, date_fin)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/covariance_matrice', methods=['POST', 'GET'])
def covariance_matrice():
    data = request.get_json()
    actif_name = data.get('actif_name')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Covariance_Matrice(actif_name, date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Risk_Minimum', methods=['POST', 'GET'])
def portefeuille_Risk_Minimum():
    data = request.get_json()
    actif_name = data.get('actif_name')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Portefeuille_Risk_Minimum(actif_name, date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Risk_Minim_Esper', methods=['POST', 'GET'])
def portefeuille_Risk_Minim_Esper():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    e0 = data.get('e0')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Portefeuille_Risk_Minim_Esper(
        actif_name, cours_cible, e0, date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/return_Risque_Frontière_Effic', methods=['POST', 'GET'])
def return_Risque_Frontière_Effic():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    e0 = data.get('e0')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = return_Risque_Frontière_Effic(
        actif_name, cours_cible, e0, date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Esper_Minimum', methods=['POST', 'GET'])
def portefeuille_Esper_Minimum():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Portefeuille_Esper_Minimum(
        actif_name, cours_cible,   date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/plot_Front_Effic', methods=['POST', 'GET'])
def plot_Front_Effic():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Plot_Front_Effic(
        actif_name, cours_cible,   date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Tangeant', methods=['POST', 'GET'])
def portefeuille_Tangeant():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    e0 = data.get('e0')
    rf = data.get('rf')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Portefeuille_Tangeant(
        actif_name, cours_cible, e0, rf,   date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Minim_Risk_Limite', methods=['POST', 'GET'])
def portefeuille_Minim_Risk_Limite():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    limit = data.get('limit')
    u = data.get('u')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Portefeuille_Minim_Risk_Limite(
        actif_name, cours_cible, u, limit, date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/Portefeuille_Minim_Risk_Limite_Esper', methods=['POST', 'GET'])
def portefeuille_Minim_Risk_Limite_Esper():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    e0 = data.get('e0')
    limit = data.get('limit')
    u = data.get('u')
    date_debut = data.get('date_debut')
    date_fin = data.get('date_fin')
    plt1 = Portefeuille_Minim_Risk_Limite_Esper(
        actif_name, cours_cible, u, limit, e0, date_debut, date_fin)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Constitution', methods=['POST', 'GET'])
def portefeuille_Constitution():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    window = data.get('window')
    Nominal = data.get('Nominal')
    Niveau = data.get('Niveau')
    plt1 = Portefeuille_Constitution(
        actif_name, cours_cible, window, Nominal, Niveau)
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/strat', methods=['POST', 'GET'])
def strat():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    date_debut_data = data.get('date_debut_data')
    date_fin_data = data.get('date_fin_data')
    window = data.get('window')
    Nominal = data.get('Nominal')
    Niveau = data.get('Niveau')
    plt1 = Strat(
        actif_name, date_debut_data, date_fin_data, cours_cible, Nominal, Niveau, window
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Constitution_OPCVM', methods=['POST', 'GET'])
def portefeuille_Constitution_OPCVM():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    date_backtest = data.get('date_backtest')
    periode_volume = data.get('periode_volume')
    rr = data.get('rr')
    Nominal = data.get('Nominal')
    Niveau = data.get('Niveau')
    plt1 = Portefeuille_Constitution_OPCVM(
        actif_name, date_backtest, periode_volume, cours_cible, Nominal, Niveau, rr
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/portefeuille_Constitution_OPCVM_test', methods=['POST', 'GET'])
def portefeuille_Constitution_OPCVM_test():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    date_backtest = data.get('date_backtest')
    periode_volume = data.get('periode_volume')
    rr = data.get('rr')
    Nominal = data.get('Nominal')
    Niveau = data.get('Niveau')
    plt1 = Portefeuille_Constitution_OPCVM_test(
        actif_name, date_backtest, periode_volume, cours_cible, Nominal, Niveau, rr
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/oPCVM_MAROC', methods=['POST', 'GET'])
def oPCVM_MAROC():
    data = request.get_json()
    actif_name = data.get('actif_name')
    cours_cible = data.get('cours_cible')
    date_backtest = data.get('date_backtest')
    taux = data.get('taux')
    periode = data.get('periode')
    Nominal = data.get('Nominal')
    Niveau = data.get('Niveau')
    plt1 = OPCVM_MAROC(
        actif_name, date_backtest, periode, cours_cible, Nominal, Niveau, taux
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/backtest', methods=['POST', 'GET'])
def backtest():
    data = request.get_json()
    actif_name = data.get('actif_name')
    date_fin_data = data.get('date_fin_data')
    date_backtest = data.get('date_backtest')
    x = data.get('x')
    Nominal = data.get('Nominal')
    MSI = data.get('MSI')
    plt1 = Backtest(
        actif_name, Nominal, x, date_backtest, date_fin_data, MSI
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/oPCVM_CHOIX', methods=['POST', 'GET'])
def oPCVM_CHOIX():
    data = request.get_json()
    actif_name = data.get('actif_name')
    periode = data.get('periode')
    date_backtest = data.get('date_backtest')
    taux = data.get('taux')
    Nominal = data.get('Nominal')
    cours_cible = data.get('cours_cible')
    plt1 = OPCVM_CHOIX(
        Nominal, actif_name, periode, date_backtest, cours_cible, taux
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/monte_Carlo', methods=['POST', 'GET'])
def monte_Carlo():
    data = request.get_json()
    actif_name = data.get('actif_name')
    periode = data.get('periode')
    date_backtest = data.get('date_backtest')
    taux = data.get('taux')
    Nominal = data.get('Nominal')
    cours_cible = data.get('cours_cible')
    date_finale = data.get('date_finale')
    b = data.get('b')
    a = data.get('a')
    MSI = data.get('MSI')
    plt1 = Monte_Carlo(
        Nominal, actif_name, periode, date_backtest, date_finale, cours_cible, taux, a, b, MSI
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1


@app.route('/oPCVM_FINALE', methods=['POST', 'GET'])
def oPCVM_FINALE():
    data = request.get_json()
    actif_name = data.get('actif_name')
    periode = data.get('periode')
    date_backtest = data.get('date_backtest')
    taux = data.get('taux')
    cours_cible = data.get('cours_cible')
    date_fin_data = data.get('date_fin_data')
    MSI = data.get('MSI')
    plt1 = OPCVM_FINALE(
        actif_name, date_backtest, date_fin_data, periode, cours_cible, taux, MSI
    )
    print(plt1)
    # my_stringIObytes = io.BytesIO()
    # plt1.figure.savefig(my_stringIObytes, format='jpg')
    # my_stringIObytes.seek(0)
    # my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return plt1
