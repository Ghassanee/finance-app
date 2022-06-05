from re import M
import numpy as np
import pandas as pd
import BVCscrap as load

class actif:
 
  def __init__(self,actif_name:str) :
    self.actif_name=actif_name
  
  def get_data(self,date_debut,date_end):
    # Return Data pandas #############
    return load.loadata(self.actif_name,start=date_debut,end=date_end)
  
  def get_intraday(self):
    # Intraday 
    # Return Data pandas #############
    return load.getIntraday(self.actif_name)

  def get_donnees_seance(self):
    
    # Données de la Scéance
    
    u=['Capitalisation', 'Cours', 'Cours de Cloture de la Veille','Devise de Cotation','Nombre de Titres','Ouverture','Plus BAS','Plus HAUT',\
       'Variation','Volume','Volume en Titres']
    v=[''] * 11   
    for i in range(11):
        v[i]=load.getCours(self.actif_name)['Données_Seance'][u[i]]
    matrix = np.array([u,v],dtype='object')
    return matrix
  
  def get_meilleur_limite(self):
    
    # Meilleur Limite
    u=['Prix Achat','Quantité Achat','Prix Vente','Quantité Vente']
    v=[''] * 4   
    for i in range(4):
        v[i]=load.getCours(self.actif_name)['Meilleur_limit'][u[i]]
    matrix = np.array([u,v],dtype='object')
    return matrix

  def get_donnees_sean_prec(self):

    # Données De La Scéance Précédante

    return pd.DataFrame(load.getCours(self.actif_name)['Seance_prec'])

  def get_dernieres_transac(self):

    # Dernière Transaction

    return pd.DataFrame(load.getCours(self.actif_name)['Dernieres_Tansaction'])
  
  def get_info_societe(self):

    # Informations Complémentaire
    
    u=['Commissaire Aux Comptes','Date de Constitution','Date Introduction','Durée Exercice Social',\
       'ISIN','Objet_social','Raison_sociale','Secteur_activité','Siege_social','Ticker']
    v=[''] * 10   
    for i in range(10):
        v[i]=load.getKeyIndicators(self.actif_name)['Info_Societe'][u[i]]
    matrix = np.array([u,v],dtype='object')
    return matrix   
  
  def Actionnaires(self):

    # Actionnaires 
    r=load.getKeyIndicators(self.actif_name)['Actionnaires']
    z=list(load.getKeyIndicators(self.actif_name)['Actionnaires'].keys())
    v=[''] * len(z)   
    for i in range(0,len(z)):
        v[i]=r[z[i]]
    matrix = np.array([z,v],dtype='object')
    return matrix
  
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

    pt=float(input('Prix de réel de Transaction ?'))
    return pt-self.get_prix_moy()
  
  def get_fourchette_effect_relat(self):

    # Fourchette Effective Relative 

    return self.get_fourchette_effect()/self.get_prix_moy()
  
  def get_corwin(self):

    # Corwin Indicator

    return (float(load.getCours(self.actif_name)['Données_Seance']['Plus haut'])-float(load.getCours(self.actif_name)['Données_Seance']['Plus bas']))/float(load.getCours(self.actif_name)['Données_Seance']['Plus haut'])

  def get_Quant_moy(self,date_deb,date_fin):
    # Volume Moyen de Transaction
    return (self.get_data(date_deb,date_fin)['Volume']*self.get_data(date_deb,date_fin)['Value']).mean()
  
  def LIX(self,date_deb,date_fin):

    # LIX Indicator
    
    import numpy as np
    return ( ( np.log( (  self.get_data(date_deb,date_fin)['Volume']*self.get_data(date_deb,date_fin)['Value']*self.get_data(date_deb,date_fin)['Value'] )/( self.get_data(date_deb,date_fin)['High']-self.get_data(date_deb,date_fin)['Low'] ) ) )).min()

  def get_indice_sect(self):

    #Indice sectorielle

    return load.getIndex()['Indices sectoriels']


  def get_indice_rentab(self):

    # Indice De Rentabilité

    return load.getIndex()['Indice rentabilite']  
