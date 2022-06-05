import numpy as np
import pandas as pd
import BVCscrap as load
from construct import Construct

from portefeuille import Portefeuille 


from actif import actif

Attijari = pd.read_excel('./docs/Attijarii.xlsx', index_col='Séance')
Itissalat = pd.read_excel('./docs/Attissalat.xlsx', index_col='Séance')
BCP = pd.read_excel('./docs/BCP.xlsx', index_col='Séance')
Lafarge = pd.read_excel('./docs/Lafarge.xlsx', index_col='Séance')
BOA = pd.read_excel('./docs/BMCE.xlsx', index_col='Séance')
Cosumar = pd.read_excel('./docs/Cosumar.xlsx', index_col='Séance')
Ciment_Maroc = pd.read_excel('./docs/Cim_Maroc.xlsx', index_col='Séance')
Marsa_Maroc = pd.read_excel('./docs/Marsa_Marooc.xlsx', index_col='Séance')
Label_Vie = pd.read_excel('./docs/LABEL_VIE.xlsx', index_col='Séance')
Taqa_Maroc = pd.read_excel('./docs/Taqa_Maroc.xlsx', index_col='Séance')
HPS = pd.read_excel('./docs/HPS.xlsx', index_col='Séance')
Total_Maroc = pd.read_excel('./docs/Total_MAROC.xlsx', index_col='Séance')
Miniere = pd.read_excel('./docs/M_touiss.xlsx', index_col='Séance')
Mutandis = pd.read_excel('./docs/Mutandis.xlsx', index_col='Séance')
Lesieur = pd.read_excel('./docs/Lesieur.xlsx', index_col='Séance')
Addoha = pd.read_excel('./docs/Addoha.xlsx', index_col='Séance')
Atlanta = pd.read_excel('./docs/Atlanta.xlsx', index_col='Séance')
Auto_Hall = pd.read_excel('./docs/Auto_Hall.xlsx', index_col='Séance')
Snep = pd.read_excel('./docs/Snepp.xlsx', index_col='Séance')
Dar_sadaa = pd.read_excel('./docs/DAR_SADAA.xlsx', index_col='Séance')
MSI = pd.read_excel('./docs/mm.xlsx', index_col='Séance')


data_names = {'Attijari': Attijari, 'Itissalat': Itissalat, 'BCP': BCP, 'Lafarge': Lafarge, 'BOA': BOA, 'Cosumar': Cosumar, 'Ciment_Maroc': Ciment_Maroc, 'Marsa_Maroc': Marsa_Maroc, 'Label_Vie': Label_Vie, 'Taqa_Maroc': Taqa_Maroc,
              'HPS': HPS, 'Total_Maroc': Total_Maroc, 'Miniere': Miniere, 'Mutandis': Mutandis, 'Lesieur': Lesieur, 'Addoha': Addoha, 'Atlanta': Atlanta, 'Auto_Hall': Auto_Hall, 'Snep': Snep, 'Dar_Sadaa': Dar_sadaa, 'MSI': MSI}

Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']


 
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

def getInfo(actif_name,option):
  dd=actif(actif_name)
  if option == "Intraday":
     return dd.get_intraday()
  elif option == "Meilleure limite":
    return dd.get_meilleur_limite
  elif option == "Données seance":
    return dd.get_donnees_seance()
  elif option == "Donnee seance precedente":
    return dd.get_donnees_sean_prec() 
  elif option == "Dernieres tansaction":
    return dd.get_dernieres_transac() 
  elif option == "Plus forte hausse":
    return dd.recap_Plus_Forte_Hausse() 
  elif option == "Plus forte baisse":
    return dd.recap_Plus_Forte_Baisse() 
  elif option == "Actionnaires":
    return dd.Actionnaires() 
  elif option == "Ratio":
    return dd.Get_Ratio() 
  elif option == "Chiffres cles":
    return dd.get_meilleur_limite 
  elif option == "Seance precedente":
    return dd.get_donnees_sean_prec() 
 
def getIndicatorDeLiquidity(actif_name,ind,dated,datef):
  dd=actif(actif_name)
  if ind=="Fourchette affichee":
    return dd.get_fourchette_affichee()
  elif ind=="Prix moyen":
    return dd.get_prix_moy()
  elif ind=="Fourchette relative":
    return dd.get_fourchette_relat()
  elif ind=="Fourchette effective relative":
    return dd.get_fourchette_effect_relat()
  elif ind=="Corwin":
    return dd.get_corwin()
  elif ind=="Quant_moy":
    return dd.get_Quant_moy(dated,datef)
  elif ind=="LIX":
    return dd.LIX(dated,datef)

def getIndice(indice_n):
  dd=actif('Attijariwafa')
  if indice_n=="Resume des indices":
    return dd.resume_index()
  elif indice_n=="Volume Global":
    return dd.recap_volume()
  elif indice_n=="Indice rentabilite":
    return dd.get_indice_rentab() 
  elif indice_n=="Indices en devises":
    return dd.get_indice_sect()
  elif indice_n=="Volume Global":
    return dd.recap_volume() 
  elif indice_n=="Volume Global":
    return dd.recap_volume() 
  elif indice_n=="Volume Global":
    return dd.recap_volume() 
  elif indice_n=="Volume Global":
    return dd.recap_volume() 
  elif indice_n=="Ponderations":
    return dd.get_pond()   

def getVisualisation(actif_name):
  a=Portefeuille(data_names)
  return a.Plot_Actif_Line(actif_name)

def getPlotIndicateurMa(actif_name,llst):
  a=Portefeuille(data_names)
  return a.Plot_Indicateur_MA(actif_name,llst)

def getDrawDown(actif_n,minmax):
  a=Portefeuille(data_names)
  return a.Plot_Indicateur_Drawdown(actif_n,minmax)

def getCombinaisaon(str1,lst1,lst2):
  a=Portefeuille(data_names)
  return a.Combinaison_Indicateurs(str1,lst1,lst2)

def getRendement(lst1,dated,datef,str1):
  a=Portefeuille(data_names)
  return a.Calcul_Rendement_Actifs(lst1,str1,dated,datef,False)  

def getRendementHist(actif_name):
  a=Portefeuille(data_names)
  return a.Plot_Histogramme(actif_name)

def getRisqueActif(str1,dated,datef):
  a=Portefeuille(data_names)
  return a.Risque_Actif(str1,dated,datef)

def getCovMat(lst1,dated,datef,plt):
  a=Portefeuille(data_names)
  if plt=='Non':
    return a.Covariance_Matrice(lst1,dated,datef,plot=False)
  elif plt=='Oui':
    return a.Covariance_Matrice(lst1,dated,datef,plot=True) 

def getPortefeuilleRiskMinimum():
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Portefeuille_Risk_Minimum(d,Cours_cible)

def getPortRiskEsp(number):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Portefeuille_Risk_Minim_Esper(d,Cours_cible,number)      

def getPortMarch(nb1,nb2):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Portefeuille_Tangeant(d,Cours_cible,nb1,nb2)  

def getFrontEffic(t=None):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Plot_Front_Effic(d,Cours_cible)

def getRiskMinim(nb,vect):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Portefeuille_Minim_Risk_Limite(d,Cours_cible,vect,nb)

def getPortOpti1(nb1,nb2,vect):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Portefeuille_Minim_Risk_Limite_Esper(d,Cours_cible,vect,nb1,nb2)

def getPortOpti2(nb1,nb2,nb3):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return  a.Portefeuille_Constitution(d,Cours_cible,nb1,nb2,nb3,1)

def getNivFixeV(dateback,periode,nominal,niveau,taux):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.OPCVM_MAROC(d,dateback,periode,Cours_cible,nominal,niveau,taux)

def getNivFixeB(datef,dateback,periode,nominal,niveau,taux):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Backtest(d,nominal,a.OPCVM_MAROC(d,datef,periode,Cours_cible,nominal,niveau,taux),dateback,datef,MSI)

def getNivVar(dateback,periode,nominal,niveau,taux):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.OPCVM_CHOIX(nominal,d,periode,dateback,Cours_cible,taux,niveau,1)

def getNivVarB(datef,dateback,periode,nominal,niveau,taux):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.Backtest(d,nominal,a.OPCVM_CHOIX(nominal,d,periode,dateback,Cours_cible,taux,niveau,2),dateback,datef,MSI)

def getMonteCarlo(datef,dateback,periode,nominal,niveau,taux,imin,imax):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.OPCVM_FINALE(d,dateback,datef,periode,Cours_cible,taux,MSI,niveau,nominal,imin,imax)

