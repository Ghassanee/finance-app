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

from functions import Calcul_Rendement_Actifs, Combinaison_Indicateurs, Covariance_Matrice, Plot_Actif_Line, Plot_Front_Effic, Plot_Histogramme, Plot_Indicateur_Drawdown, Plot_Indicateur_MA, Portefeuille_Esper_Minimum, Portefeuille_Risk_Minim_Esper, Portefeuille_Risk_Minimum, Risque_Actif, get_indicator_de_liquidity, get_indice, get_info

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
