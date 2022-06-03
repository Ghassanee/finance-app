from re import M
from unittest import result
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import BVCscrap as load
from numpy.linalg import inv
import cvxpy as cv 


data1={'---':'---'}
df1=pd.DataFrame(data1)
data2={'---':'---'}
df2=pd.DataFrame(data2)
data3={'---':'---'}
df3=pd.DataFrame(data3)
data4={'---':'---'}
df4=pd.DataFrame(data4)
data5={'---':'---'}
df5=pd.DataFrame(data5)
data6={'---':'---'}
df6=pd.DataFrame(data6)
data7={'---':'---'}
df7=pd.DataFrame(data7)
data8={'---':'---'}
df8=pd.DataFrame(data8)
data9={'---':'---'}
df9=pd.DataFrame(data9)
data10={'---':'---'}
df10=pd.DataFrame(data10)
data11={'---':'---'}
df11=pd.DataFrame(data11)
data12={'---':'---'}
df12=pd.DataFrame(data12)
data13={'---':'---'}
df13=pd.DataFrame(data13)
data14={'---':'---'}
df14=pd.DataFrame(data14)
data15={'---':'---'}
df15=pd.DataFrame(data15)
data16={'---':'---'}
df16=pd.DataFrame(data16)
data17={'---':'---'}
df17=pd.DataFrame(data17)
data18={'---':'---'}
df18=pd.DataFrame(data18)
data19={'---':'---'}
df19=pd.DataFrame(data19)
data20={'---':'---'}
df20=pd.DataFrame(data20)
data21={'---':'---'}
df21=pd.DataFrame(data21)
data22={'---':'---'}
df22=pd.DataFrame(data22)
data23={'---':'---'}
df23=pd.DataFrame(data23)

frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df19,df19,df20,df21,df22]
result = pd.concat(frames)   


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

class actif:
  import BVCscrap as load
  import pandas as pd

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


class Portefeuille:

  def __init__(self,data_names):
    self.data_names=data_names 
    

  def Plot_Actif_Line(self,actif:str):
    # Visualisation des prix d Actif

    if actif == 'MSI':
      self.data_names[actif]['Instrument'].plot(figsize=(17,7))
    else :
      self.data_names[actif]['COURS_CLOTURE'].plot(figsize=(17,7))
    
  def Plot_Indicateur_MA(self,actif:str,longueur:list):

    # Visualisation : Prix + Indicateur Moyenne Mobile 
    # a=Portefeuille(data_names)
    # a.Plot_Indicateur_MA('Attijari',[100,50,133])
    
    d=pd.DataFrame()
    d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']

    for i in range(0,len(longueur)):
      d['MA : {} '.format(longueur[i])]=self.data_names[actif]['COURS_CLOTURE'].rolling(longueur[i]).mean()
    
    d[list(d.columns)].plot(figsize=(17,7))

  def Plot_Indicateur_Drawdown(self,actif:str,tp):

    # Visualisation : Prix + Indicateur Max/Min Drawdown
    # a=Portefeuille(data_names)
    # a.Plot_Indicateur_Drawdown('MSI','Min')

    d=pd.DataFrame()

    if actif=='MSI':
      if tp in ['max','max'.title(),'max'.upper()] :
        d['cmMax']=self.data_names[actif]['Instrument'].cummax()
        d['COURS_CLOTURE']=self.data_names[actif]['Instrument']
        d[['cmMax','COURS_CLOTURE']].plot(figsize=(17,7))

      elif tp in ['min','min'.title(),'min'.upper()]  :
        d['cmMin']=self.data_names[actif]['Instrument'].cummin()
        d['COURS_CLOTURE']=self.data_names[actif]['Instrument']
        d[['cmMin','COURS_CLOTURE']].plot(figsize=(17,7))

    else :
      if tp in ['max','max'.title(),'max'.upper()] :
        d['cmMax']=self.data_names[actif]['COURS_CLOTURE'].cummax()
        d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']
        d[['cmMax','COURS_CLOTURE']].plot(figsize=(17,7))

      elif tp in ['min','min'.title(),'min'.upper()]  :
        d['cmMin']=self.data_names[actif]['COURS_CLOTURE'].cummin()
        d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']
        d[['cmMin','COURS_CLOTURE']].plot(figsize=(17,7))


  def Combinaison_Indicateurs(self,actif,cible_indicateur:list,longueur_MA=None):
    
    # Combinaison entre deux Indicateurs : Moyenne Mobile + Max/Min Drawdown
    # a.Combinaison_Indicateurs('Attijari',['MA','Max','Min'],[100,200,50])  

    d=pd.DataFrame()
    d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']

    for i in cible_indicateur:

      if i in ['max','max'.title(),'max'.upper()]:
        d['cmMax']=self.data_names[actif]['COURS_CLOTURE'].cummax()
        
      elif i in ['min','min'.title(),'min'.upper()]  :
        d['cmMin']=self.data_names[actif]['COURS_CLOTURE'].cummin()
          
      elif i in ['Ma','ma','MA']:

        if longueur_MA == None :
          longueur_MA=[50]

        for i in range(0,len(longueur_MA)):
          d['MA : {} '.format(longueur_MA[i])]=self.data_names[actif]['COURS_CLOTURE'].rolling(longueur_MA[i]).mean()
      
    d[list(d.columns)].plot(figsize=(17,7))

 
  def Calcul_Rendement_Actifs(self, actif:list , tp2:str , date_debut , date_fin ,tp=True ) :
    
    # Rendement des Actifs 
    # a=Portefeuille(data_names)
    # a.Calcul_Rendement_Actifs(['Attijari','BOA','Snep'],'2020-10-10','2022-01-01','Cumulatif',False)
    # tp est toujours = False ( pour ne pas changer la data originale )


    y=[]
    for i in range(0,len(actif)):
      #if i in list(self.data_names.keys()):
      y.append(self.data_names[actif[i]])
    
    if tp == True  :
      if tp2 == 'Quotidien':
        for i in range(0,len(y)):
          y[i]['Rendement']=(y[i]['COURS_CLOTURE'].pct_change())
       
          
      elif tp2 == 'Cumulatif':
        for i in range(0,len(y)):
          y[i]['Rendement_Cumul']=((y[i]['COURS_CLOTURE'].pct_change())+1).cumprod()
     
    elif tp == False:
      d=pd.DataFrame()

      if tp2=='Quotidien':
        for i in range(0,len(actif)):
          d['Rendement {}'.format(actif[i])]=(self.data_names[actif[i]]['COURS_CLOTURE'].loc[date_debut:date_fin]).pct_change()
        return d
        
      elif tp2 == 'Cumulatif':
        for i in range(0,len(actif)):
          d['Rendement_Cumul {}'.format(actif[i])]=(self.data_names[actif[i]].loc[date_debut:date_fin]['COURS_CLOTURE'].pct_change()+1).cumprod()
        return d

  def Plot_Histogramme(self,actif):
    
    # Visualisation du rendement des Actifs en Histogramme
    # a=Portefeuille(data_names)
    # a.Plot_Histogramme('MSI')


    if actif == 'MSI':
      (self.data_names[actif]['Instrument'].pct_change()).hist(figsize=(13,7),bins=600)
    else :
      (self.data_names[actif]['COURS_CLOTURE'].pct_change()).hist(figsize=(13,7),bins=600)


  def Risque_Actif(self,actif,date_debut,date_fin):

    # Calcul du Risque des Actif pendant la periode : date_debut et date_fin 
    # a=Portefeuille(data_names)
    # a.Risque_Actif('BCP','2021-01-01','2022-01-01')

    ee=pd.DataFrame()
    if actif == 'MSI':
      ee['Rendement']=self.data_names[actif]['Instrument'].loc[date_debut:date_fin].pct_change()
    else : 
      ee['Rendement']=self.data_names[actif]['COURS_CLOTURE'].loc[date_debut:date_fin].pct_change()
    
    
    return 'Risque_Actif {} : {} % '.format(actif,(ee.std()[0]*np.sqrt(252)*100))
    


  def Covariance_Matrice(self,actif:list,date_debut,date_fin,plot=False):

      # Calcul de la matrice de variance covariance entre plusieurs actifs
      # Ploter la dispertion en cas de plot == True 
      # On va intégrer deux boutton , pour le calcul et pour la visualisation de la dispertion
      # a=Portefeuille(data_names)
      # a.Covariance_Matrice(['Attijari','BOA','Snep','Addoha'],'2020-01-01','2022-01-01',plot=True)


      if plot==False:
        return self.Calcul_Rendement_Actifs(actif,'Quotidien',date_debut,date_fin,False).cov()
      elif plot == True :
        from pandas.plotting import scatter_matrix
        scatter_matrix(self.Calcul_Rendement_Actifs(actif,'Quotidien',date_debut,date_fin,False),hist_kwds={'bins':600},alpha=0.8,figsize=(17,9))
        plt.show()
  
    


class Construct:

  def __init__(self,data_names):
    self.data_names=data_names 

  
  def Calcul_Rendement_Actifs(self, actif:list , tp2:str ,tp=True):
    y=[]
    for i in range(0,len(actif)):
      #if i in list(self.data_names.keys()):
      y.append(self.data_names[actif[i]])
    


    if tp == True  :
      if tp2 == 'Quotid':
        for i in range(0,len(y)):
          y[i]['Rendement']=(y[i]['COURS_CLOTURE'].pct_change())
          

      elif tp2 == 'Cumul':
        for i in range(0,len(y)):
          y[i]['Rendement_Cumul']=((y[i]['COURS_CLOTURE'].pct_change())+1).cumprod()
          

    elif tp == False:

      d=pd.DataFrame()

      if tp2=='Quotid':
        for i in range(0,len(actif)):
          d['Rendement {}'.format(actif[i])]=y[i]['COURS_CLOTURE'].pct_change()
        return d
        

      elif tp2 == 'Cumul':
        for i in range(0,len(actif)):
          d['Rendement_Cumul {}'.format(actif[i])]=(y[i]['COURS_CLOTURE'].pct_change()+1).cumprod()
        return d
    
  def Plot_Histogramme(self,actif,cible):
    actif[cible].hist(figsize=(17,7),bins=600)

  def Risque_Actif(self,actif):
    return 'Risque_Actif : {} % '.format((self.Calcul_Rendement(actif,'Quotid',False)['Rendement'].std()*100))
  
  def Rendement_Actif(self,actif,tp2:str,tp=True):
    if tp==True:
      if tp2=='Quotid':
        actif['Rendement']=actif['COURS_CLOTURE'].pct_change()
        return actif
      elif tp2=='Cumul':
        actif['Rendement_Cumul']=(actif['COURS_CLOTURE'].pct_change()+1).cumprod()
        return actif

    if tp == False :
      d=pd.DataFrame()
      if tp2=='Quotid':
        d['Rendement_Actif']=actif['COURS_CLOTURE'].pct_change()
        return d
      if tp2=='Cumul':
        d['Rendement_Cumul']=(actif['COURS_CLOTURE'].pct_change()+1).cumprod()
        return d
  

  def Covariance_Matrice(self,actif:list,cours_cible,plot=False):
      if plot==False:
        return self.Calcul_Rendement_Actifs(actif,'Quotid',False).cov()
      elif plot == True :
        from pandas.plotting import scatter_matrix
        scatter_matrix(self.Calcul_Rendement_Actifs(actif,'Quotid',False),hist_kwds={'bins':600},alpha=0.8,figsize=(17,7))
        plt.show()


################################################## Partie Constructeur ####################################################
## Dans tout le Code : 
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # Actifs =['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    



  def Portefeuille_Risk_Minimum(self,actif:list,cours_cible):

    # Portefeuille qui nous garentit le risque minimum ( sans aucune contrainte )
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # a.Portefeuille_Risk_Minimum(d,Cours_cible,'2020-01-01','2022-05-18')
    
    V= self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    a=np.dot(V_inv,e)
    p=np.dot(np.dot(e.T,V_inv),e)
    x=a/p
    u1=['']*len(actif)
    for i in range(0,len(actif)):
      u1[i]='{} : {} % '.format(actif[i],round(x[i]*100,3))
    data = {'Le portefeuille qui garentit le minimum de risque ':u1
        }
    df1 = pd.DataFrame(data)
    Vecteur_Esper=[]    
    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
    data2 = {'On a bien une somme de ':100*(a/p).sum(),
             'Le niveau de risque minimum': 100*np.dot(np.dot((a/p).T,V),(a/p).T)**0.5,
             'Le Rendement Espéré de votre Portefeuille':100*np.dot(Vecteur_Esper,(a/p))             
        }
 
    df2 = pd.DataFrame(data2)  
    frames = [df1,df2]
    result = pd.concat(frames)
    return result



  def Portefeuille_Risk_Minim_Esper(self,actif:list,cours_cible,E0):
  
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]
    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)
    Vecteur_Esper=np.array(Vecteur_Esper)

    A=np.dot(np.dot(e.T,V_inv),Vecteur_Esper)
    B=np.dot(np.dot(Vecteur_Esper.T,V_inv),Vecteur_Esper)
    C=np.dot(np.dot(e.T,V_inv),e)
    
    D=(B*C)-(A*A)
    
    w1=((C*E0)-A)
    w2=(B-(A*E0))

    a=w1*np.dot(V_inv,Vecteur_Esper)
    b=w2*np.dot(V_inv,e)
    o=(1/D)*(a+b)

    u1=['']*len(actif)

    for i in range(0,len(actif)):
      u1[i]='{} : {} % '.format(actif[i],o[i]*100)

    data = {'Le Portefeuille qui vous garentit le risque minimum à votre Espérance espéré':u1
        }
 
    df1 = pd.DataFrame(data)
    
    print('On a bien ') 
    print( '{}  %' .format(100*(1/D)*(a+b).sum() ) )
    print('\n')
    
    print('Votre Niveau de Risque ')
    print('{} %' .format(100*np.dot(np.dot(((1/D)*(a+b)).T,V),((1/D)*(a+b)).T)**0.5 )    )
    print('\n')

    print('Votre Rendement est bien :')
    print("{} %" .format(100*np.dot(o,Vecteur_Esper) )  )

    data2 = {'On a bien ':100*(1/D)*(a+b).sum(),
             'Le niveau de risque mnimum': 100*np.dot(np.dot(((1/D)*(a+b)).T,V),((1/D)*(a+b)).T)**0.5,
             'Le Rendement Espéré de votre Portefeuille':100*np.dot(o,Vecteur_Esper)             
        }
 
    df2 = pd.DataFrame(data2)  
    frames = [df1,df2]
    result = pd.concat(frames)
    return result



 

  def Return_Risque_Frontière_Effic(self,actif:list,cours_cible,E0):

    # Fonction qui nous retourne le risque minimum pour une Espérance de Rendement donnée ( Pas de boutton dans les interfaces graphique )
    
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    A=np.dot(np.dot(e.T,V_inv),Vecteur_Esper)
    B=np.dot(np.dot(Vecteur_Esper.T,V_inv),Vecteur_Esper)
    C=np.dot(np.dot(e.T,V_inv),e)
    
    D=(B*C)-(A*A)
    
    w1=((C*E0)-A)
    w2=(B-(A*E0))

    a=w1*np.dot(V_inv,Vecteur_Esper)
    b=w2*np.dot(V_inv,e)
    o=(1/D)*(a+b)

    return np.dot(np.dot(((1/D)*(a+b)).T,V),((1/D)*(a+b)).T)**0.5



  def Portefeuille_Esper_Minimum(self,actif:list,cours_cible):

    # Fonction qui nous retourne le rendement maximum pour un risque donné ( Pas de boutton dans les interfaces graphique )

    V= self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    a=np.dot(V_inv,e)
    p=np.dot(np.dot(e.T,V_inv),e)

    x=a/p
    

    Vecteur_Esper=[]
    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
    
    return np.dot(Vecteur_Esper,(a/p))





  def Plot_Front_Effic(self,actif:list,cours_cible ):

    risque_minim= self.Return_Risque_Frontière_Effic( actif, cours_cible,self.Portefeuille_Esper_Minimum(actif,cours_cible)  )

    risque=[risque_minim,self.Return_Risque_Frontière_Effic( actif, cours_cible,  self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.01 ),
            self.Return_Risque_Frontière_Effic(actif,cours_cible,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.02 ),
            self.Return_Risque_Frontière_Effic(actif,cours_cible,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.03) ,
            self.Return_Risque_Frontière_Effic(actif,cours_cible,self.Portefeuille_Esper_Minimum(actif,cours_cible )+0.04 ),
            self.Return_Risque_Frontière_Effic(actif,cours_cible,self.Portefeuille_Esper_Minimum(actif,cours_cible )+0.05  ),
            self.Return_Risque_Frontière_Effic(actif,cours_cible,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.06 )  ]

    rendement=[
               self.Portefeuille_Esper_Minimum(actif,cours_cible)
              ,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.01
               ,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.02
               ,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.03
               ,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.04
               ,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.05
               ,self.Portefeuille_Esper_Minimum(actif,cours_cible)+0.06  ]

    plt.figure(figsize=(18,8))
    plt.plot(risque,rendement,'*-',c='r')
    plt.xlabel('Risque ')
    plt.ylabel('Rendement Espéré ')
    plt.title('La Frontière Efficiente des {} Actifs : {}  '.format(len(actif),actif))



  def Portefeuille_Tangeant(self,actif:list,cours_cible,E0,Rf):
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]
    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    A=np.dot(np.dot(e.T,V_inv),Vecteur_Esper)
    B=np.dot(np.dot(Vecteur_Esper.T,V_inv),Vecteur_Esper)
    C=np.dot(np.dot(e.T,V_inv),e)

    a=np.dot(e.T,Rf)
    m=Vecteur_Esper-a
    
    h=np.dot(V_inv,m)
    
    b=E0-Rf
    
    k=B-(2*A*Rf)+(C*Rf*Rf)
    
    y=b/k
    pend=np.dot(h.T,y)

    u1=['']*20

    for i in range(0,20):
      u1[i]='{} : {} % '.format(actif[i],pend[i])
    
    data = {'Ponderation de l actif Risqué ':u1} 
    df1 = pd.DataFrame(data)
    rendement=np.dot(pend.T,Vecteur_Esper)
    pp=1-(np.dot(pend.T,e))
    rend_portefeuille=pp*Rf+rendement
    risque = (np.dot(np.dot(pend,V),pend)**0.5)
    data2 = {'Rendement de votre Portefeuille Risqué':np.dot(pend.T,Vecteur_Esper),
             'Ponderation de l actif sans Risque': 1-(np.dot(pend.T,e)) ,
             'Somme des Ponderations de votre Portefeuille Risqué ':pend.sum(),
	           'On a bien La somme des Ponderations': 1-np.dot(pend.T,e)+pend.sum(),
	           'Rendement Espéré Total de votre Portefeuille':rend_portefeuille,
             'Risque': risque
             } 
    df2 = pd.DataFrame(data2)  
    frames = [df1,df2]
    result = pd.concat(frames)
    return result





  def Portefeuille_Minim_Risk_Limite(self,actif:list,cours_cible,u,limite):

    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)
    Vecteur_Esper=np.array(Vecteur_Esper)

    import cvxpy as cv
    x=cv.Variable(len(actif))
    contrainte = [cv.sum(x) == 1,
               x <= 1,
               x >= 0 # Pas de Vente à découvert
              ]

    rend=x @ Vecteur_Esper
    risk = cv.quad_form(x, V)
    contrainte += [
                 
                 x @ u == limite # Somme des actifs choisi doit etre égale == limite
      ]
    objective = cv.Minimize(risk)
    prob = cv.Problem(objective, contrainte)
    a=prob.solve('ECOS')
    c= x.value


    u1=['']*len(actif)

    for i in range(0,len(actif)):
      u1[i]='{} : {} '.format(actif[i],c[i])
    
    data = {'Le Portefeuille qui Vous Garantit Le Risque Minimum est ':u1
        }
 
    df1 = pd.DataFrame(data)

    data2 = {'Risque Minimum':np.dot(np.dot(c,V),c)**0.5,
             'Somme des Ponderations': c.sum(),
             'La contrainte de Pondération est bien respectée':np.dot(c,u),
	     'Votre Rendement': np.dot(c,Vecteur_Esper),
	       }
 
    df2 = pd.DataFrame(data2)  
    frames = [df1,df2]
    result = pd.concat(frames)
    return result





  def Portefeuille_Minim_Risk_Limite(self,actif:list,cours_cible,u,limite):

    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)
    Vecteur_Esper=np.array(Vecteur_Esper)

    import cvxpy as cv
    x=cv.Variable(len(actif))
    contrainte = [cv.sum(x) == 1,
               x <= 1,
               x >= 0 # Pas de Vente à découvert
              ]

    rend=x @ Vecteur_Esper
    risk = cv.quad_form(x, V)
    contrainte += [
                 
                 x @ u == limite # Somme des actifs choisi doit etre égale == limite
      ]
    objective = cv.Minimize(risk)
    prob = cv.Problem(objective, contrainte)
    a=prob.solve('ECOS')
    c= x.value


    u1=['']*len(actif)

    for i in range(0,len(actif)):
      u1[i]='{} : {} '.format(actif[i],c[i])


    data = {'Le Portefeuille qui Vous Garantit Le Risque Minimum est ':u1
        }
 
    df1 = pd.DataFrame(data)

    data2 = {'Risque Minimum':np.dot(np.dot(c,V),c)**0.5,
             'Somme des Ponderations': c.sum(),
             'La contrainte de Pondération est bien respectée':np.dot(c,u),
	     'Votre Rendement': np.dot(c,Vecteur_Esper),
	       }
 
    df2 = pd.DataFrame(data2)  
    frames = [df1,df2]
    result = pd.concat(frames)
    return result


  def Portefeuille_Minim_Risk_Limite_Esper(self,actif:list,cours_cible,u,limite,E0):
 
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)
    Vecteur_Esper=np.array(Vecteur_Esper)

    import cvxpy as cv
    x=cv.Variable(len(actif))

    contrainte = [cv.sum(x) == 1,
               x <= 1,
               x >= 0,
               x @ Vecteur_Esper == E0,
               x @ u == limite
              ]
    rend=x @ Vecteur_Esper
    risk = cv.quad_form(x, V)
    objective = cv.Minimize(risk)
    prob = cv.Problem(objective, contrainte)
    a=prob.solve()


    if prob.status == 'infeasible':
      print('Solution ne converge pas ! Contraintes Contradictoires  !!!! ')
      print('\n')
      print('Problème au Niveau de votre espérance de Rendement souhaité ')
      return #dir chi erreur hna o bla tfelsif

    c= x.value

    u1=['']*len(actif)

    for i in range(0,len(actif)):
      u1[i]='{} : {} '.format(actif[i],c[i])


    data = {'Portefeuille adéquat à votre Rendement':u1
        }
 
    df1 = pd.DataFrame(data)

    data2 = {'Rendement Espéré':np.dot(c,Vecteur_Esper),
             'Somme des Ponderations': c.sum(),
             'Risque de portefeuille':np.dot(np.dot(c,V),c)**0.5,
	     'Contrainte De pondérations est Bien Respectée': np.dot(c,u).sum(),
        }
 
    df2 = pd.DataFrame(data2)  
    frames = [df1,df2]
    result = pd.concat(frames)
    return result




  def Portefeuille_Constitution(self,actif:list,cours_cible,window,Nominal,Niveau,cas):
    
    # Fonction qui nous donne le portefeuille optimal ( avec une contraine de liquidité )
    # Pas de Vente à Découvert 
    # On calcule la moyenne du volume observé dans un intervale de taille : window en commençant avec la dernière date téléchargée dans notre dataset .

    import cvxpy as cv 

    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
  
    Contr=[]

    for j in range(0,len(actif)) :
      Contr.append( ( self.data_names[actif[j]].tail(window)['VOLUME'].mean()* Niveau  )/ Nominal )

    u1=['']*len(actif)

    for k in range(0,len(actif)):
      u1[k]='{}  :  {}  '.format(actif[k],Contr[k])


    data = {'Les niveaux a ne pas depasser ':u1
        }
 
    df1 = pd.DataFrame(data)



  
    x=cv.Variable(len(actif))

    contrainte = [cv.sum(x) == 1,
               x <= 1,
               x >= 0 
              ]

    rend= x @ Vecteur_Esper

    risk = cv.quad_form(x, V)

    for h in range(0,len(actif)):
      contrainte += [
                   
                   x[h] <= Contr[h]
          ]


    objective = cv.Minimize(risk)

    prob = cv.Problem(objective, contrainte)

    a=prob.solve('ECOS')
    
    c= x.value

    print('\n')
    if prob.status == 'infeasible':
      print('Solution ne Converge pas !! \n ')
      print('Contrainte Budgétaire Non Respectée !')
      return #chi erreur
    
    print('\n')
    print('Le Portefeuille qui vous garantit le risque Minimum est :')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} '.format(actif[i],c[i]))
    print('\n')

    u2=['']*len(actif)

    for i in range(0,len(actif)):
      u2[i]='{} : {} '.format(actif[i],c[i])


    data2 = {'Portefeuille minim ':u2
        }
 
    df2 = pd.DataFrame(data2)

    data3 = {'Risque Minimum':np.dot(np.dot(c,V),c)**0.5,
             'Somme des Ponderations': c.sum(),
	       }
 
    df3 = pd.DataFrame(data3)  
    frames = [df1,df2,df3]
    result = pd.concat(frames)
    if cas==1:
      return c
    elif cas==2:
      return result





  def Strat(self,actif:list,date_debut_data:str,date_fin_data:str,cours_cible,Nominal,Niveau,window):

    # Stratégie pour repondérer notre Portefeuille si un de nos actifs détenu atteint son cours Cible ( Atteint son Espérance de Rendement )
    # La stratégie marche entre les deux dates : date_debut_data et date_end_data 

    c=self.Portefeuille_Constitution(actif,cours_cible,window,Nominal,Niveau,2)
    mm=[]

    for i in range(0,len(actif)):
      mm.append(self.data_names[actif[i]].loc[date_debut_data:date_fin_data]['COURS_CLOTURE'])
    

    for i in range(0,len(mm)):
      Portefeuillee_Penderation = pd.concat(mm,axis=1)
    
    Portefeuillee_Penderation.columns = actif

    for i in range(0,len(c)):
      Portefeuillee_Penderation[actif[i]]=Portefeuillee_Penderation[actif[i]]*c[i]

    Portefeuillee_Penderation.dropna(axis=0,inplace=True)

    #print(Portefeuillee_Penderation)

    m=[]

    for i in range(0,len(actif)):
      m.append(self.data_names[actif[i]].loc[date_debut_data:date_fin_data]['COURS_CLOTURE'])
    
    for i in range(0,len(m)):
      Portefeuille = pd.concat(m,axis=1)

    Portefeuille.columns=actif
    
    Portefeuille.dropna(axis=0,inplace=True)

    #print(Portefeuille)

    finish = False

    Portefeuillee_Penderationn = pd.DataFrame()

    s=Portefeuillee_Penderation.mean().sort_values()
    
    
    ma=dict(s.iloc[len(s)-4:])
    
    print('Attention ! Ces Titre ont un prix Ponderé elevé !!! Evitez de les éliminer de votre Portefeuille ')
    print('\n')
    for i in ma.keys():
      print(i)

    
    print('\n')
    print('\n')
    for i in range(0,len(Portefeuille)):
      for j in list(Portefeuille.columns):
        
        if Portefeuille[j][i]== cours_cible[actif.index(j)] and c[actif.index(j)] != 0 :
          print(' La Date : {}  / On a {} qui atteint son Cours Cible'.format(Portefeuille.index[i],j))

          if j in ma.keys():
            print('\n')
            print(' Attention !!  {} a un Prix Ponderé Trop elevé !!  '.format(j))
            print('\n')

          reponse = input('Continue ? Merci de répondre par NON si voulez-vous éliminer cet Actif \n') 
          print('\n')
        
          if reponse in  ['NON','Non','non','no']  :
            print('Changement de Penderations : \n')
            rep=input('Strat : 1 ? /  Strat : 2 ? /  Strat : 3 ? ')
            print('\n')
            print('\n')
        
                 
            if rep=='1':
            
              print('Le premier choix choisi : Elimination du Titre {} de Votre Portefeuille et maintenir les Autres Pondérations Constantes : '.format(j))
              print('\n')
              c[actif.index(j)]=0
              for im in range(0,len(c)):
                if c[im] != 0 :
                  print('{}  :  {} '.format(Portefeuille.columns[im],c[im]))
                if c[im] == 0 :
                  print('{}  :  {}  <--------------------------------  '.format(Portefeuille.columns[im],c[im]))
            
              print('\n')
              print('\n')
              for k in range(0,len(c)):
                 if c[k]==0 :
                    Portefeuillee_Penderation[actif[k]].iloc[i:]=Portefeuillee_Penderation[actif[k]].iloc[i:]*c[k]
            
              #print(Portefeuillee_Penderation)
              Portefeuillee_Penderationn=pd.DataFrame(Portefeuillee_Penderation.sum(axis=1))
              Portefeuillee_Penderationn.columns=['Prix_Portefeuille']

              #print(Portefeuillee_Penderationn)

              Portefeuillee_Penderationn['Rendement_Cumul']=(1+Portefeuillee_Penderationn['Prix_Portefeuille'].pct_change()).cumprod()

              #Portefeuillee_Penderation.drop(labels='2022-02-10',axis=0,inplace=True)

              MSI=pd.read_excel('mm.xlsx',index_col='Séance')
              MSI=MSI.loc[date_debut_data:date_fin_data]

              #MSI.drop(labels='2022-02-10',axis=0,inplace=True)

              MSI['Rendement_Cumul']=(1+MSI['Instrument'].pct_change()).cumprod()

              Perfor=pd.concat([Portefeuillee_Penderationn['Prix_Portefeuille'],Portefeuillee_Penderationn['Rendement_Cumul'],MSI['Instrument'],MSI['Rendement_Cumul']],axis=1)
              Perfor.columns=['Prix_Portefeuille','Rendement_Cumul_Portefeuille','Prix_MSI_20','Rendement_Cumul_MSI_20']

              Perfor['MSI']=Perfor['Rendement_Cumul_MSI_20']*100
              Perfor['Portefeuille']=Perfor['Rendement_Cumul_Portefeuille']*100

              Perfor['MSI'].iloc[0]=100
              Perfor['Portefeuille'].iloc[0]=100
              
              Perfor.dropna(axis=0,inplace=True)
              #print(Perfor)
              print('\n')
              b=input('Maintenir ces pondération et Backtest ? Merci de Répondre par OUI si c est le Cas ! \n')
              if b=='OUI':
                Perfor[['MSI','Portefeuille']].plot(figsize=(17,7))
                #return Portefeuillee_Penderation
                return
            
            
            if rep=='2':

              print('Le deuxième choix choisi : Attribution de la Pondération du Titre {} au Titre qui performe le Plus : '.format(j))
              print('\n')

              print('Performance de Nos Titres jusqu à la periode : {}'.format(Portefeuille.index[i]))
              print('\n')
              op=(Portefeuille.iloc[i]/Portefeuille.iloc[0])-1
              print(op)
              print('\n')
              print('On a Bien Le Titre  : {} qui performme Le Plus '.format(list(op.index[op==op.max()])[0]))

              print('\n')

            
              c[actif.index(op.index[op==op.max()])] += c[actif.index(j)]
              c[actif.index(j)]=0
              e= c[actif.index(j)]
            
              le=[]
              le.append(c[actif.index(op.index[op==op.max()])])
              #print(le)

              for k in range(0,len(c)):
                if c[k] != 0 and c[k] !=  c[actif.index(op.index[op==op.max()])] :
                  print('{}  :  {} '.format(Portefeuille.columns[k],c[k]))
                else:
                  print('{}  :  {}  <--------------------------------  '.format(Portefeuille.columns[k],c[k]))
          

              for k in range(0,len(c)):
                if c[k]==0  : #c[k] ==  c[aa.index(op.index[op==op.max()])] :
                  Portefeuillee_Penderation[actif[k]].iloc[i:]=Portefeuillee_Penderation[actif[k]].iloc[i:]*c[k]
                if c[k] in le :
                  Portefeuillee_Penderation[actif[k]].iloc[i:] = ( Portefeuillee_Penderation[actif[k]].iloc[i:] ) + (Portefeuille[actif[k]].iloc[i:]*e)

              
              Portefeuillee_Penderationn=pd.DataFrame(Portefeuillee_Penderation.sum(axis=1))
              Portefeuillee_Penderationn.columns=['Prix_Portefeuille']

              #p rint(Portefeuillee_Penderationn)

              Portefeuillee_Penderationn['Rendement_Cumul']=(1+Portefeuillee_Penderationn['Prix_Portefeuille'].pct_change()).cumprod()

              #Portefeuillee_Penderation.drop(labels='2022-02-10',axis=0,inplace=True)

              MSI=pd.read_excel('mm.xlsx',index_col='Séance')
              MSI=MSI.loc[date_debut_data:date_fin_data]

              #MSI.drop(labels='2022-02-10',axis=0,inplace=True)

              MSI['Rendement_Cumul']=(1+MSI['Instrument'].pct_change()).cumprod()

              Perfor=pd.concat([Portefeuillee_Penderationn['Prix_Portefeuille'],Portefeuillee_Penderationn['Rendement_Cumul'],MSI['Instrument'],MSI['Rendement_Cumul']],axis=1)
              Perfor.columns=['Prix_Portefeuille','Rendement_Cumul_Portefeuille','Prix_MSI_20','Rendement_Cumul_MSI_20']

              Perfor['MSI']=Perfor['Rendement_Cumul_MSI_20']*100
              Perfor['Portefeuille']=Perfor['Rendement_Cumul_Portefeuille']*100

              Perfor['MSI'].iloc[0]=100
              Perfor['Portefeuille'].iloc[0]=100
              
              #Perfor.dropna(axis=0,inplace=True)
              #print(Perfor
              print('\n')
              b=input('Maintenir ces pondération et Backtest ? Merci de Répondre par OUI si c est le Cas ! \n')
              if b=='OUI':
                Perfor[['MSI','Portefeuille']].plot(figsize=(17,7))
                #return Portefeuillee_Penderation
                return




            if rep=='3' : 
              print('Le troisième choix choisi : Attribution équi-penderée : ')
              print('\n')
              e=c[actif.index(j)]/len(c)
              print('La proportion à ajouter : {} '.format(e))
              print('\n')
              print('\n')
            
              for k in range(0,len(c)):
                c[k] += e
            
              c[actif.index(j)]=0
           
              for iz in range(0,len(c)):
                if c[iz] != 0 :
                  print('{}  :  {} '.format(Portefeuille.columns[iz],c[iz]))
                if c[iz] == 0 :
                  print('{}  :  {}  <--------------------------------  '.format(Portefeuille.columns[iz],c[iz]))
              print('\n')
              print('\n')
            
              #print('L indice à partir on fait nos changement : {}'.format(i))
              #print('\n')

              for k in range(0,len(c)):
                if c[k]==0 : #or c[k] in le :#c[k] ==  c[aa.index(op.index[op==op.max()])] :
                  Portefeuillee_Penderation[actif[k]].iloc[i:] = Portefeuillee_Penderation[actif[k]].iloc[i:]*c[k]
              
              for k in range(0,len(c)):
                if c[k] !=0 : #or c[k] in le :#c[k] ==  c[aa.index(op.index[op==op.max()])] :
                  Portefeuillee_Penderation[actif[k]].iloc[i:] = ( Portefeuillee_Penderation[actif[k]].iloc[i:] ) + (Portefeuille[actif[k]].iloc[i:]*e)
              
              
              
              Portefeuillee_Penderationn=pd.DataFrame(Portefeuillee_Penderation.sum(axis=1))
              Portefeuillee_Penderationn.columns=['Prix_Portefeuille']

              #print(Portefeuillee_Penderationn)

              Portefeuillee_Penderationn['Rendement_Cumul']=(1+Portefeuillee_Penderationn['Prix_Portefeuille'].pct_change()).cumprod()

              #Portefeuillee_Penderation.drop(labels='2022-02-10',axis=0,inplace=True)

              MSI=pd.read_excel('mm.xlsx',index_col='Séance')
              MSI=MSI.loc[date_debut_data:date_fin_data]

              #MSI.drop(labels='2022-02-10',axis=0,inplace=True)

              MSI['Rendement_Cumul']=(1+MSI['Instrument'].pct_change()).cumprod()

              Perfor=pd.concat([Portefeuillee_Penderationn['Prix_Portefeuille'],Portefeuillee_Penderationn['Rendement_Cumul'],MSI['Instrument'],MSI['Rendement_Cumul']],axis=1)
              Perfor.columns=['Prix_Portefeuille','Rendement_Cumul_Portefeuille','Prix_MSI_20','Rendement_Cumul_MSI_20']

              Perfor['MSI']=Perfor['Rendement_Cumul_MSI_20']*100
              Perfor['Portefeuille']=Perfor['Rendement_Cumul_Portefeuille']*100

              Perfor['MSI'].iloc[0]=100
              Perfor['Portefeuille'].iloc[0]=100
              
              #Perfor.dropna(axis=0,inplace=True)
              #print(Perfor)


              b=input('Maintenir ces pondération et Backtest ? Merci de Répondre par OUI si c est le Cas ! \n')
              if b=='OUI':
                Perfor[['MSI','Portefeuille']].plot(figsize=(17,7))
                #return Portefeuillee_Penderation
                return






  

  def Portefeuille_Constitution_OPCVM(self,actif:list,date_backtest,periode_volume,cours_cible,Nominal,Niveau,rr,cas):
    
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
  

    Contr=[]

    print('Les Niveaux à ne pas dépacer ')
    print('\n')
    for j in range(0,len(actif)) :
      Contr.append( ( self.data_names[actif[j]].loc[:date_backtest].tail(periode_volume)['VOLUME'].mean()* Niveau  )/ Nominal )
    
    so=np.array(Contr).sum()
    #print('so : {}'.format(so))
    

    if so > 1 and so <= 1.31 :
      u= 1.37-np.array(Contr).sum() 
      for i in range(0,len(Contr)):
        Contr[i]=Contr[i]+u*( Contr[i]/np.array(Contr).sum() )

      #print('u : {}'.format(u))

    u1=['']*len(Contr)
    for i in range(0,len(Contr)):
      u1[i]='{} : {} '.format(actif[i],Contr[i])
    data = {'Les niveaux a ne pas depasser':u1
        } 
    df1 = pd.DataFrame(data)
    for i in range(0,len(Contr)):
      print('{} : {}'.format(actif[i],Contr[i]))
   
    data2 = {'Somme des contraines': np.array(Contr).sum()
        } 
    df2 = pd.DataFrame(data2)


   
    print('\n')
    ok = np.array([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    x=cv.Variable(len(actif))

   
    contrainte = [cv.sum(x) == 1,
               x <= 1,
               x >= 0 
              ]
    
    

    rend= x @ Vecteur_Esper

    risk = cv.quad_form(x, V)

    for h in range(0,len(actif)):
      contrainte += [
                   
                   x[h] <= Contr[h]
          ]

    contrainte += [

            x[actif.index('Attijari')] <= 0.20,
           x[actif.index('Itissalat')] <= 0.15,
           x @ ok <= 0.45      

        ] 
    
    objective = cv.Minimize(risk)
    prob = cv.Problem(objective, contrainte)
    a=prob.solve('ECOS')

    c= x.value
  
    u3=['']*len(actif)
    for i in range(0,len(actif)):
      u3[i]='{} : {} '.format(actif[i],c[i])
    data3 = {'Portefeuille risque min':u3
        } 
    df3 = pd.DataFrame(data3)


    print('\n')
    print('Le Portefeuille qui vous garantit le risque Minimum est :')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} '.format(actif[i],c[i]))
    print('\n')
    
    data4 = {'Somme des 4 premieres val':c[0]+c[1]+c[2]+c[3]
        } 
    df4 = pd.DataFrame(data4)

    print('Somme des 4 premières valeurs : {}'.format(c[0]+c[1]+c[2]+c[3]))
    print('\n')

    if 'Attijari' in actif :
      print('  = {}  <  {} '.format(c[actif.index('Attijari')],0.20))
      print('\n')
      data5 = {'On a bien la Ponderation de Attijari':[c[actif.index('Attijari')],0.20]
        } 
      df5 = pd.DataFrame(data5)

    if 'Itissalat' in actif :
      print('On a bien la Ponderation de Itissalat  = {}  <  {}'.format(c[actif.index('Itissalat')],0.15))
      print('\n')
      data6 = {'On a bien la Ponderation de Itissalat':[c[actif.index('Itissalat')],0.15]
        } 
      df6 = pd.DataFrame(data6)
    

    print('Le Risque Minimum est : ')
    print(np.dot(np.dot(c,V),c)**0.5)
    data7 = {'Risque min ':np.dot(np.dot(c,V),c)**0.5
        } 
    df7 = pd.DataFrame(data7)    
    mp=np.dot(np.dot(c,V),c)**0.5
    print('\n')

    print('On a Bien la somme des Penderation est : ')
    print(c.sum())
    print('\n')

    data8 = {'Sum ponderations ':c.sum()
        } 
    df8 = pd.DataFrame(data8) 


    print('Pas de Vente à Découvert  ! ! ! ')
    print('\n')

    indice=[]
    f=[]
    
    u9=['']*len(c)
    for i in range(0,len(c)):
      if c[i]>0.1:
        print('l actif {} a une ponderation de {} '.format(actif[i],c[i]))
        f.append(c[i])
        indice.append(i)
        u9[i]='l actif {} a une ponderation de {} '.format(actif[i],c[i])
        data9 = {'Portefeuille adéquat à votre Rendement':u9
                  } 
        df9 = pd.DataFrame(data9)
    
    print('\n')
    print('La somme des titres qui dépace 0.1 est {}'.format(np.array(f).sum()))
    print('\n')

    data10 = {'La somme des titres qui dépace 0.1 est': np.array(f).sum()
        } 
    df10 = pd.DataFrame(data10)    
    if np.array(f).sum() <= 0.45 and cas==2:
      return c

    if np.array(f).sum() > 0.45 and cas==1 :
      print('Il nous reste {} - 0.45 = {} à éliminer '.format(np.array(f).sum(),np.array(f).sum()-0.45))
      data11 = {'Il nous reste à éliminer':'{} - 0.45 = {}'.format(np.array(f).sum(),np.array(f).sum()-0.45)
        }
      df11 = pd.DataFrame(data11)
      print('\n')     
      
      print('Elimination proportionelle :')
      print('\n')

      u12=['']*len(f)  
      for i in range(0, len(f)):
        u12[i]='Le Titre {} va perdre {} de {}'.format(actif[indice[i]],f[i]/np.array(f).sum(),np.array(f).sum()-0.45)
        data12 = {'Elimination proportionnelle':u12
                      }
        df12 = pd.DataFrame(data12)
        
        print('Le Titre {} va perdre {} de {}'.format(actif[indice[i]],f[i]/np.array(f).sum(),np.array(f).sum()-0.45))
          
      for k in indice : 
        c[k] = c[k]-((np.array(f).sum()-0.45)*(f[indice.index(k)]/np.array(f).sum()))

      print('\n')
      u13=['']*len(c)
      for k in range(0,len(c)):
        if k in indice :
          u13[k]='{} : {}  <--------------- '.format(actif[k],c[k])
          data13 = {'--------':u13
                  }
          df13 = pd.DataFrame(data)


          print('{} : {}  <--------------- '.format(actif[k],c[k]))
        else :
          u13[k]='{} : {}  <--------------- '.format(actif[k],c[k])
          data13 = {'--------':u13
                  }
          df13 = pd.DataFrame(data)
      ll=[]
      for k in range(0,len(c)):
        if k in indice :
          ll.append(c[k])
      print('\n')
      print('On a bien la somme des Titres qui dépacent 0.1 est : {} <= 0.45'.format(np.array(ll).sum()))
      print('\n')
      print('Votre Nouveau Risque est : {}'.format(np.dot(np.dot(c,V),c)**0.5))
      print('\n')
      print('On a bien {} < {} risque avant élimination '.format(np.dot(np.dot(c,V),c)**0.5,mp))
      print('\n')
      print('Votre investissement sera : {} en Portefeuille Risqué et {} en Actif sans Risque '.format(np.array(c).sum(),rr))
      print('\n')
      
    data14 = {'somme des Titres qui dépacent 0.1':np.array(ll).sum(),
             'Nouveau Risque': np.dot(np.dot(c,V),c)**0.5,
             'Risque avant elimination':'{} < {}'.format(np.dot(np.dot(c,V),c)**0.5,mp),
	     '-------': 'Votre investissement sera : {} en Portefeuille Risqué et {} en Actif sans Risque '.format(np.array(c).sum(),rr),
        } 
    df14 = pd.DataFrame(data14) 

    frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14]
    result = pd.concat(frames)  
    if cas==1:
      return result
    elif cas==2:
      return c
 




  def Portefeuille_Constitution_OPCVM_test(self,actif:list,date_backtest,periode_volume,cours_cible,Nominal,Niveau,rr,cas):
    
    import cvxpy as cv 

    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
  

    Contr=[]

    print('Les Niveaux à ne pas dépacer ')
    print('\n')
    for j in range(0,len(actif)) :
      Contr.append( ( self.data_names[actif[j]].loc[:date_backtest].tail(periode_volume)['VOLUME'].mean()* Niveau  )/ Nominal )
    
    u1=['']*len(actif)
    for i in range(0,len(actif)):
      u1[i]='{} : {} '.format(actif[i],Contr[i])
    data = {'Les niveaux a ne pas depasser':u1
        } 
    df1 = pd.DataFrame(data) 
    print('\n')

    data2 = {'Somme des contraines': np.array(Contr).sum()
        } 
    df2 = pd.DataFrame(data2) 

   
    print('Somme  : {} \n'.format(np.array(Contr).sum()))
    print('\n')

    indice_attijari=[]
    if 'Attijari' in actif :
      for i in range(0,len(Contr)) :
        if actif[i]=='Attijari':
          indice_attijari.append(i)
      
      if Contr[indice_attijari[0]] >= 0.2 :
        rest=Contr[indice_attijari[0]]-0.2
        Contr[indice_attijari[0]] = 0.2 
        data3 = {'Attijari est suponderé de': rest
        }
        df3 = pd.DataFrame(data3) 

        print('Attijari est suponderé de {}'.format(rest))
        print('\n')
        print('Le reste : {} : répartition proportionelle '.format(rest))
        print('\n')
        data4 = {'Les reste': rest
        }
        df4 = pd.DataFrame(data4)
        for im in range(indice_attijari[0]+1,len(Contr)):
          Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
        u5=['']*len(Contr)
        for k in range(0,len(Contr)):
          u5[k]='{} : {} '.format(actif[k],Contr[k])
        data = {'Repartition proportionelle':u5
        }
        df5 = pd.DataFrame(data5)
      #print('Somme : {}'.format(np.array(Contr).sum()))
      else :
        data6 = {'---------': 'La ponderation de Attijari : {} < 0.2'.format(Contr[actif.index('Attijari')])
        }
        df6 = pd.DataFrame(data6)
        print('La ponderation de Attijari : {} < 0.2'.format(Contr[actif.index('Attijari')]))

    indice_Itissalat=[]
    if 'Itissalat' in actif :
      for i in range(0,len(Contr)) :
        if actif[i]=='Itissalat':
          indice_Itissalat.append(i)
      if Contr[indice_Itissalat[0]] >= 0.15 :
        rest=Contr[indice_Itissalat[0]]-0.15
        Contr[indice_Itissalat[0]] = 0.15
        print('\n')
        print('Itissalat est suponderé de {}'.format(rest))
        print('\n')
        print('Le reste : {} : répartition proportionelle '.format(rest))
        print('\n')
        data7 = {'---------': 'Itissalat est suponderé de {}'.format(rest),
                 '---------': 'Le reste : {} : répartition proportionelle '.format(rest)
        }
        df7 = pd.DataFrame(data7)
        for im in range(indice_Itissalat[0]+1,len(Contr)):
          Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
        print('\n')
        u8=['']*len(Contr)
        for k in range(0,len(Contr)):
          print('{}  :  {}  '.format(actif[k],Contr[k]))
          u8[i]='{} : {} '.format(actif[k],Contr[k])
        data8 = {'Les niveaux a ne pas depasser':u8
                  }
        df8 = pd.DataFrame(data8)
      else :
        print('\n')
        print('La ponderation de Itissalat : {} < 0.15'.format(Contr[actif.index('Itissalat')]))
        print('\n')
        data9 = {'-----------': 'La ponderation de Itissalat : {} < 0.15'.format(Contr[actif.index('Itissalat')])
        } 
        df9 = pd.DataFrame(data9)
      #print('Somme : {}'.format(np.array(Contr).sum()))         


      f=[]
      indice=[]
      for i in range(0,len(Contr)):
        if Contr[i]>=0.1:
          f.append(Contr[i])
          indice.append(i)
      

      print('\n')
      
      ss=np.array(f).sum()

      if ss > 0.45 :
        print('On a une surponderation de somme de titres qui dépacent 0.1')
        print('\n')
        u10=['']*len(indice)
        for i in indice :
          print('Le Titre : {} a une pondération de {}'.format(actif[i],Contr[i]))
          u10[i]='{} : {} '.format(actif[i],Contr[i])
        data10 = {'-------':u10
        }
        df10 = pd.DataFrame(data10)  
          
        print('\n')
        print('La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum()))
        re=ss-0.45
        print('\n')
        print('Le reste : {} = {} - 0.45 répartition proportionelle '.format(re,ss))
        print('\n')
        data11 = {'---------': 'La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum()),
                 '---------': 'Le reste : {} = {} - 0.45 répartition proportionelle '.format(re,ss)
        }
        df11 = pd.DataFrame(data11)
        for ik in indice:
          Contr[ik]=Contr[ik]-(ss-0.45)*(f[indice.index(ik)]/np.array(f).sum())
        
        for im in range(0,len(Contr)):
          if im in indice :
            Contr[im]=Contr[im]
          else :
            Contr[im] = Contr[im] + (ss-0.45)*(  Contr[im]/(np.array(Contr).sum()*4)  )
      
      else :
        print('On a la somme des titre qui dépacent 0.10  =  {}'.format(np.array(f).sum()))
        print('\n')
        data12 = {'--------':'On a la somme des titre qui dépacent 0.10  =  {}'.format(np.array(f).sum())
        }
        df12 = pd.DataFrame(data12)  

      
      u13=['']*len(Contr)
      for k in range(0,len(Contr)):
        u13[k]='{} : {} '.format(actif[k],Contr[k])
      data13 = {'---------':u13
        }
      df13 = pd.DataFrame(data13)
      
     
      #print('La somme est {}'.format(np.array(Contr).sum()))
      
      sm=np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])
      
      if sm <=0.45:
        data14 = {'--------':'La somme des 4 premières valeurs {} <= 0.45'.format(sm)
        } 
        df14 = pd.DataFrame(data14)
      else :
        data15 = {'--------':'La somme des 4 premières valeurs {} > 0.45'.format(sm)
        } 
        df15 = pd.DataFrame(data15) 
        data16 = {'--------':'Répartition proportionnelle de {} - 0.45 = {}'.format(sm,sm-0.45)
        } 
        df16 = pd.DataFrame(data16)                 
        for ik in range(0,4):
          Contr[ik]=Contr[ik]-(sm-0.45)*(Contr[ik]/np.array(Contr[:4]).sum())
        for ikk in range(5,len(Contr)):
          Contr[ikk]=Contr[ikk]+(sm-0.45)/5
        

        print('\n')
        u17=['']*len(Contr)
        for k in range(0,len(Contr)):
          u17[k]='{} : {} '.format(actif[k],Contr[k])
        data17 = {'---------':u17
        }
        df17 = pd.DataFrame(data17)
        print('\n')
        data18 = {'--------':'On a bien la somme des 4 premières valeurs {} <= 0.45'.format(np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3]))
        } 
        df18 = pd.DataFrame(data18)        
      print('\n')
      if np.array(Contr).sum()>1 :
        ed=np.array(Contr).sum()-1
        for i in range(0,len(Contr)):
          Contr[i]=Contr[i]-ed*(Contr[i]/np.array(Contr).sum())
      print('la somme : {}'.format(np.array(Contr).sum()))
      data19 = {'--------':'la somme : {}'.format(np.array(Contr).sum())
          } 
      df19 = pd.DataFrame(data19)   

      frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19]
      result = pd.concat(frames)  
      if cas==1:
        return result
      elif cas==2:
        return np.array(Contr)   
      

    

 
  
  def OPCVM_MAROC(self,actif,date_backtest,periode,Cours_cible,nominal,niveau,taux):
    
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((Cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    Contr=[]

    for j in range(0,len(actif)) :
      Contr.append( ( self.data_names[actif[j]].tail(periode)['VOLUME'].mean()* niveau  )/ nominal )
    
    so=np.array(Contr).sum()
    


    if so <= 1.17:
      return self.Portefeuille_Constitution_OPCVM_test(actif,date_backtest,periode,Cours_cible,nominal,niveau,taux,1)
    
    if so > 1.17  :
      return self.Portefeuille_Constitution_OPCVM(actif,date_backtest,periode,Cours_cible,nominal,niveau,taux,1)
          
    



  

  def Backtest(self,actif:str,nominal,x,date_backtest,date_fin_data,MSI):
    
    prix=[]
    prix_prem=[]
    nbr=[]
    Portefeuille=pd.DataFrame()

    nominal=nominal*np.array(x).sum()
    print('\n')

    data12 = {'Nominal du Backtest':nominal
                      }
    df12 = pd.DataFrame(data12)


    print('Nominal du Backtest : {} '.format(nominal))
    print('\n')
    print('\n')
    for i in range(0,len(actif)) :
      prix.append(self.data_names[actif[i]]['COURS_CLOTURE'].loc[date_backtest:])

    Portefeuille = pd.concat(prix,axis=1)
    Portefeuille.columns=actif

    for i in list(Portefeuille.columns):
      prix_prem.append(Portefeuille[i].iloc[0])

    for i in range(0,len(prix_prem)):
      nbr.append((x[i]*nominal)/prix_prem[i])

    evol=[]

    for i in range(0,len(list(Portefeuille.columns))):
      evol.append(Portefeuille[actif[i]]*nbr[i])

    Evolution=pd.concat(evol,axis=1)
    Evolution.dropna(inplace=True)
    Evolution_finale=pd.DataFrame()
    Evolution_finale['Price']=Evolution.sum(axis=1)



    Evolution_finale['Rendement_Cumul']=(1+Evolution_finale['Price'].pct_change()).cumprod()

    MSI=MSI.loc[date_backtest:date_fin_data]
    MSI['Rendement_Cumul']=(1+MSI['Instrument'].pct_change()).cumprod()

    concat=pd.concat(  [ MSI['Rendement_Cumul'],Evolution_finale['Rendement_Cumul']  ] ,axis=1)
    concat.columns=['Portefeuille','Benchmark']

    concat['Portefeuille']=concat['Portefeuille']*100
    concat['Benchmark']=concat['Benchmark']*100

    concat['Portefeuille'].iloc[0]=100
    concat['Benchmark'].iloc[0]=100


    concat[['Portefeuille','Benchmark']].loc[date_backtest:date_fin_data].plot(figsize=(17,7))

    V=self.Covariance_Matrice(actif,False)
    print('\n')
    #print('Risque Espéré de notre Portefeuille : {}'.format(np.dot(np.dot(x,V),x)**0.5))
    print('\n')
    print('Risque Observé de Portefeuille : {} '.format((Evolution_finale['Price'].pct_change()).std()))
    print('Risque Observé de Benchmark : {} '.format((MSI['Instrument'].loc[date_backtest:date_fin_data].pct_change()).std()))
    print('\n')
    print('\n')

    data14 = {'Risque Observé de Portefeuille':(Evolution_finale['Price'].pct_change()).std(),
             'Risque Observé de Benchmark': (MSI['Instrument'].loc[date_backtest:date_fin_data].pct_change()).std(),
              } 
    df14 = pd.DataFrame(data14)

    return concat[['Portefeuille','Benchmark']].loc[date_backtest:date_fin_data].plot(figsize=(17,7))







  def OPCVM_CHOIX(self,nominal,actif,periode,date_backtest,cours_cible,taux,niveau,cas):

    niveau={}

    # for i in actif : 
    #   niveau[i]=float(input('Niveau de liquidité choisi pour : {}  ? \n'.format(i)))

        
    V=self.Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    Contr=[]

    for j in range(0,len(actif)) :
      Contr.append( ( self.data_names[actif[j]].tail(periode)['VOLUME'].mean()* niveau[actif[j]]  )/ nominal )
    
    so=np.array(Contr).sum()

    if so <= 1.17:
      
      import cvxpy as cv 

      V=self.Covariance_Matrice(actif,False)
      V_inv=inv(V)
      e=np.ones(len(actif))

      Vecteur_Esper=[]

      for i in range(0,len(actif)):
        Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

      Vecteur_Esper=np.array(Vecteur_Esper)
  

      Contr=[]

      print('Les Niveaux à ne pas dépacer ')
      print('\n')
      for j in range(0,len(actif)) :
        Contr.append( ( self.data_names[actif[j]].loc[:date_backtest].tail(periode)['VOLUME'].mean()* niveau[actif[j]]  )/ nominal )
    

      u1=['']*len(actif)
      for i in range(0,len(actif)):
        u1[i]='{} : {} '.format(actif[i],Contr[i])
      data = {'Les niveaux a ne pas depasser':u1
          } 
      df1 = pd.DataFrame(data) 
      print('\n')

      print('\n')
    
   
      print('Somme  : {} \n'.format(np.array(Contr).sum()))
      print('\n')
      data2 = {'Somme': np.array(Contr).sum()
        } 
      df2 = pd.DataFrame(data2) 

      indice_attijari=[]
      if 'Attijari' in actif :
        for i in range(0,len(Contr)) :
          if actif[i]=='Attijari':
            indice_attijari.append(i)
      
        if Contr[indice_attijari[0]] >= 0.2 :
          rest=Contr[indice_attijari[0]]-0.2
          Contr[indice_attijari[0]] = 0.2 
          print('Attijari est suponderé de {}'.format(rest))
          print('\n')
          data3 = {'Attijari est suponderé de': rest
           }
          df3 = pd.DataFrame(data3)
          print('Le reste : {} : répartition proportionelle '.format(rest))
          print('\n')
          data4 = {'Les reste': rest
            }
          df4 = pd.DataFrame(data4)
          for im in range(indice_attijari[0]+1,len(Contr)):
            Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
          for k in range(0,len(Contr)):
            print('{}  :  {}  '.format(actif[k],Contr[k]))
        #print('Somme : {}'.format(np.array(Contr).sum()))
        else :
          print('La ponderation de Attijari : {} < 0.2'.format(Contr[actif.index('Attijari')]))
          data6 = {'---------': 'La ponderation de Attijari : {} < 0.2'.format(Contr[actif.index('Attijari')])
            }
          df6 = pd.DataFrame(data6)
      indice_Itissalat=[]
      if 'Itissalat' in actif :
        for i in range(0,len(Contr)) :
          if actif[i]=='Itissalat':
            indice_Itissalat.append(i)
        if Contr[indice_Itissalat[0]] >= 0.15 :
          rest=Contr[indice_Itissalat[0]]-0.15
          Contr[indice_Itissalat[0]] = 0.15
          print('\n')
          print('Itissalat est suponderé de {}'.format(rest))
          print('\n')
          print('Le reste : {} : répartition proportionelle '.format(rest))
          print('\n')
          data7 = {'---------': 'Itissalat est suponderé de {}'.format(rest),
                   '---------': 'Le reste : {} : répartition proportionelle '.format(rest)
                }
          df7 = pd.DataFrame(data7)
          for im in range(indice_Itissalat[0]+1,len(Contr)):
            Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
          print('\n')
          for k in range(0,len(Contr)):
            print('{}  :  {}  '.format(actif[k],Contr[k]))
        else :
          print('\n')
          print('La ponderation de Itissalat : {} < 0.15'.format(Contr[actif.index('Itissalat')]))
          print('\n')
          data9 = {'-----------': 'La ponderation de Itissalat : {} < 0.15'.format(Contr[actif.index('Itissalat')])
           } 
          df9 = pd.DataFrame(data9)         
        #print('Somme : {}'.format(np.array(Contr).sum()))         


        f=[]
        indice=[]
        for i in range(0,len(Contr)):
          if Contr[i]>=0.1:
            f.append(Contr[i])
            indice.append(i)
      

        print('\n')
      
        ss=np.array(f).sum()

        if ss > 0.45 :
          print('On a une surponderation de somme de titres qui dépacent 0.1')
          print('\n')
          for i in indice :
            print('Le Titre : {} a une pondération de {}'.format(actif[i],Contr[i]))
          print('\n')
          u10=['']*len(indice)
          for i in indice :
            print('Le Titre : {} a une pondération de {}'.format(actif[i],Contr[i]))
            u10[i]='{} : {} '.format(actif[i],Contr[i])
          data10 = {'-------':u10
            }
          df10 = pd.DataFrame(data10) 
          print('La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum()))
          re=ss-0.45
          print('\n')
          print('Le reste : {} = {} - 0.45 répartition proportionelle '.format(re,ss))
          print('\n')
          data11 = {'---------': 'La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum()),
                    '---------': 'Le reste : {} = {} - 0.45 répartition proportionelle '.format(re,ss)
                }
          df11 = pd.DataFrame(data11)  
          for ik in indice:
            Contr[ik]=Contr[ik]-(ss-0.45)*(f[indice.index(ik)]/np.array(f).sum())
        
          for im in range(0,len(Contr)):
            if im in indice :
              Contr[im]=Contr[im]
            else :
              Contr[im] = Contr[im] + (ss-0.45)*(  Contr[im]/(np.array(Contr).sum()*4)  )
      
        else :
          print('On a la somme des titre qui dépacent 0.10  =  {}'.format(np.array(f).sum()))
          print('\n')
          data12 = {'--------':'On a la somme des titre qui dépacent 0.10  =  {}'.format(np.array(f).sum())
            }
          df12 = pd.DataFrame(data12)  
      
      
        for k in range(0,len(Contr)):
           print('{}  :  {}  '.format(actif[k],Contr[k]))
      
        print('\n')
        u13=['']*len(Contr)
        for k in range(0,len(Contr)):
          u13[k]='{} : {} '.format(actif[k],Contr[k])
          data13 = {'---------':u13
           }
        df13 = pd.DataFrame(data13)
      
     
        #print('La somme est {}'.format(np.array(Contr).sum()))
      
        sm=np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])
      
        if sm <=0.45:
          print('La somme des 4 premières valeurs {} <= 0.45'.format(sm))
          data14 = {'--------':'La somme des 4 premières valeurs {} <= 0.45'.format(sm)
            } 
          df14 = pd.DataFrame(data14)
        else :
          print('La somme des 4 premières valeurs {} > 0.45'.format(sm))
          print('Répartition proportionnelle de {} - 0.45 = {}'.format(sm,sm-0.45))
          data15 = {'--------':'La somme des 4 premières valeurs {} > 0.45'.format(sm)
            } 
          df15 = pd.DataFrame(data15) 
          data16 = {'--------':'Répartition proportionnelle de {} - 0.45 = {}'.format(sm,sm-0.45)
            } 
          df16 = pd.DataFrame(data16)
          for ik in range(0,4):
            Contr[ik]=Contr[ik]-(sm-0.45)*(Contr[ik]/np.array(Contr[:4]).sum())
          for ikk in range(5,len(Contr)):
            Contr[ikk]=Contr[ikk]+(sm-0.45)/5
        

          print('\n')
          for k in range(0,len(Contr)):
            print('{}  :  {}  '.format(actif[k],Contr[k]))
          u17=['']*len(Contr)
          for k in range(0,len(Contr)):
            u17[k]='{} : {} '.format(actif[k],Contr[k])
          data17 = {'---------':u17
            }
          df17 = pd.DataFrame(data17)  
          print('\n')
          print('On a bien la somme des 4 premières valeurs {} <= 0.45'.format(np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])))
          data18 = {'--------':'On a bien la somme des 4 premières valeurs {} <= 0.45'.format(np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3]))
            } 
          df18 = pd.DataFrame(data18)  
        print('\n')
        if np.array(Contr).sum()>1 :
          ed=np.array(Contr).sum()-1
          for i in range(0,len(Contr)):
            Contr[i]=Contr[i]-ed*(Contr[i]/np.array(Contr).sum())
        print('la somme : {}'.format(np.array(Contr).sum()))
        data19 = {'--------':'la somme : {}'.format(np.array(Contr).sum())
        }         
        df19 = pd.DataFrame(data19) 
        if cas==1:
          return result
        elif cas==2:
          return np.array(Contr) 

      

        
    
    if so > 1.17  :
      
      import cvxpy as cv 
      V=self.Covariance_Matrice(actif,False)
      V_inv=inv(V)
      e=np.ones(len(actif))

      Vecteur_Esper=[]

      for i in range(0,len(actif)):
        Vecteur_Esper.append((cours_cible[i]/self.data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

      Vecteur_Esper=np.array(Vecteur_Esper)
  

      Contr=[]

      print('Les Niveaux à ne pas dépacer ')
      print('\n')
      for j in range(0,len(actif)) :
        Contr.append( ( self.data_names[actif[j]].loc[:date_backtest].tail(periode)['VOLUME'].mean()* niveau[actif[j]]  )/ nominal )
    
      so=np.array(Contr).sum()
      print('so : {}'.format(so))
    

      if so > 1 and so <= 1.31 :
        u= 1.34-np.array(Contr).sum() 
        for i in range(0,len(Contr)):
          Contr[i]=Contr[i]+u*( Contr[i]/np.array(Contr).sum() )

        print('u : {}'.format(u))

      print('\n')
      for i in range(0,len(Contr)):
        print('{} : {}'.format(actif[i],Contr[i]))
      u1=['']*len(actif)
      for i in range(0,len(actif)):
        u1[i]='{} : {} '.format(actif[i],Contr[i])
      data = {'Les niveaux a ne pas depasser':u1
        } 
      df1 = pd.DataFrame(data) 

      print('\n')
      print('La Somme des contraintes : {} '.format(np.array(Contr).sum()))
      print('\n')
      data2 = {'Somme des contraines': np.array(Contr).sum()
        } 
      df2 = pd.DataFrame(data2) 
    

    
      print('\n')
      ok = np.array([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
      x=cv.Variable(len(actif))

   
      contrainte = [cv.sum(x) == 1,
               x <= 1,
               x >= 0
              ]
    
    

      rend= x @ Vecteur_Esper

      risk = cv.quad_form(x, V)

      for h in range(0,len(actif)):
        contrainte += [
                   
                   x[h] <= Contr[h]
          ]

      contrainte += [

            x[actif.index('Attijari')] <= 0.20,
           x[actif.index('Itissalat')] <= 0.15,
           x @ ok <= 0.45      

        ] 
    
      objective = cv.Minimize(risk)
      prob = cv.Problem(objective, contrainte)
      a=prob.solve('ECOS')

      c= x.value

      if prob.status == 'infeasible' :
        print('Fonction dédiée pour les nominal >= 90 000 000 DHS')
        print(' statut de Problème : {} !!!!'.format(prob.status))
        data20 = {'-------': 'Fonction dédiée pour les nominal >= 90 000 000 DHS',
                  ' statut de Problème : {} !!!!':prob.status
        } 
        df20 = pd.DataFrame(data20) 
        if nominal >= 20000000 and nominal < 50000000:
          return self.Portefeuille_Constitution_OPCVM(actif,date_backtest,periode,cours_cible,nominal,0.3,taux)
        if nominal >= 50000000:
          return self.Portefeuille_Constitution_OPCVM(actif,date_backtest,periode,cours_cible,nominal,1,taux)
        
  
      print('\n')
      print('Le Portefeuille qui vous garantit le risque Minimum est :')
      print('\n')
      for i in range(0,len(actif)):
        print('{} : {} '.format(actif[i],c[i]))
      print('\n')
      u3=['']*len(actif)
      for i in range(0,len(actif)):
        u3[i]='{} : {} '.format(actif[i],Contr[i])
      data3 = {'Portefeuille risk min':u1
        } 
      df3 = pd.DataFrame(data3) 
      print('\n')
      print('Somme des 4 premières valeurs : {}'.format(c[0]+c[1]+c[2]+c[3]))
      print('\n')
      data4 = {'--------':'La somme des 4 premières valeurs {} <= 0.45'.format(sm)
        } 
      df4 = pd.DataFrame(data4)

      if 'Attijari' in actif :
        print('On a bien la Ponderation de Attijari  = {}  <  {} '.format(c[actif.index('Attijari')],0.20))
        print('\n')
        data6 = {'---------': 'Ponderation de Attijari  = {}  <  {} '.format(c[actif.index('Attijari')],0.20)
        }
        df6 = pd.DataFrame(data6)

      if 'Itissalat' in actif :
        print('On a bien la Ponderation de Itissalat  = {}  <  {}'.format(c[actif.index('Itissalat')],0.15))
        print('\n')
        data7 = {'---------': 'Ponderation de Itissalat  = {}  <  {} '.format(c[actif.index('Itissalat')],0.15)
        }
        df7 = pd.DataFrame(data7)
    

      print('Le Risque Minimum est : ')
      print(np.dot(np.dot(c,V),c)**0.5)
      mp=np.dot(np.dot(c,V),c)**0.5
      print('\n')

      print('On a Bien la somme des Penderation est : ')
      print(c.sum())
      print('\n')
      data8 = {'Le Risque Minimum est : ':np.dot(np.dot(c,V),c)**0.5,
                'Somme des ponderations':c.sum()
        }
      df8 = pd.DataFrame(data8)      

      print('Pas de Vente à Découvert  ! ! ! ')
      print('\n')

      indice=[]
      f=[]
      u9=['']*len(c)
      for i in range(0,len(c)):
        if c[i]>0.1:
          print('l actif {} a une ponderation de {} '.format(actif[i],c[i]))
          u9[i]='l actif {} a une ponderation de {} '.format(actif[i],c[i])
          f.append(c[i])
          indice.append(i)
      data9 = {'-------':u9
        }
      df9 = pd.DataFrame(data9)
      print('\n')
      print('La somme des titres qui dépace 0.1 est {}'.format(np.array(f).sum()))
      print('\n')
      data11 = {'---------': 'La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum())
           }
      df11 = pd.DataFrame(data11)
      if np.array(f).sum() <= 0.45 and cas==2:
        return c

      if np.array(f).sum() > 0.45 :
        print('Il nous reste {} - 0.45 = {} à éliminer '.format(np.array(f).sum(),np.array(f).sum()-0.45))
        data12 = {'---------': 'Il nous reste {} - 0.45 = {} à éliminer '.format(np.array(f).sum(),np.array(f).sum()-0.45),
                  '----------': 'Elimination proportionelle :' }
        df12 = pd.DataFrame(data12)
        print('\n')
     
      
        print('Elimination proportionelle :')
        print('\n')

        u13=['']*len(f)
        for i in range(0,len(f)):
          u13[i]='Le Titre {} va perdre {} de {}'.format(actif[indice[i]],f[i]/np.array(f).sum(),np.array(f).sum()-0.45)

        data13 = {'---------':u13
        }
        df13 = pd.DataFrame(data13)
        for i in range(0, len(f)):
          print('Le Titre {} va perdre {} de {}'.format(actif[indice[i]],f[i]/np.array(f).sum(),np.array(f).sum()-0.45))
          
        for k in indice : 
          c[k] = c[k]-((np.array(f).sum()-0.45)*(f[indice.index(k)]/np.array(f).sum()))

        print('\n')
        
        u14=['']*len(c)
        for k in range(0,len(c)):
          if k in indice :
            print('{} : {}  <--------------- '.format(actif[k],c[k]))
            u14[k]='{} : {}  <--------------- '.format(actif[k],c[k])
          else :
            print('{} : {} '.format(actif[k],c[k]))
            u14[k]='{} : {}  <--------------- '.format(actif[k],c[k])
        data14 = {'---------':u14
        }
        df14 = pd.DataFrame(data14)
        ll=[]
        for k in range(0,len(c)):
          if k in indice :
            ll.append(c[k])
        print('\n')
        print('On a bien la somme des Titres qui dépacent 0.1 est : {} <= 0.45'.format(np.array(ll).sum()))
        print('\n')
        print('Votre Nouveau Risque est : {}'.format(np.dot(np.dot(c,V),c)**0.5))
        print('\n')
        print('On a bien {} < {} risque avant élimination '.format(np.dot(np.dot(c,V),c)**0.5,mp))
        print('\n')
        print('Votre investissement sera : {} en Portefeuille Risqué et {} en Actif sans Risque '.format(np.array(c).sum(),taux))
        print('\n')
        data15 = {'--------':'On a bien la somme des Titres qui dépacent 0.1 est : {} <= 0.45'.format(np.array(ll).sum()),
        '-----':'Votre Nouveau Risque est : {}'.format(np.dot(np.dot(c,V),c)**0.5),
        '------':'On a bien {} < {} risque avant élimination '.format(np.dot(np.dot(c,V),c)**0.5,mp),
        '-------':'Votre investissement sera : {} en Portefeuille Risqué et {} en Actif sans Risque '.format(np.array(c).sum(),taux)
        }
        df15 = pd.DataFrame(data15) 
        frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df19,df19,df20]
        result = pd.concat(frames)   
        if cas==1:
          return result
        elif cas==2:
          return c  

  def Monte_Carlo(self,nominal,actif,periode,date_backtest,date_finale,cours_cible,taux,a,b,MSI):
    
    #OPCVM_MAROC(self,actif,date_backtest,periode,Cours_cible,nominal,niveau,taux)
    rend={}
    x=[]

    for i in range(0,50):
      niveau=float(np.random.uniform(a,b,1))
      print('Niveau : {}'.format(niveau))
      x=self.OPCVM_MAROC(actif,date_backtest,periode,cours_cible,nominal,niveau,taux)
          
      prix=[]
      prix_prem=[]
      nbr=[]
      Portefeuille=pd.DataFrame()

      for i in range(0,len(actif)) :
        prix.append(self.data_names[actif[i]]['COURS_CLOTURE'].loc[date_backtest:date_finale])

      Portefeuille = pd.concat(prix,axis=1)
      Portefeuille.columns=actif

      for i in list(Portefeuille.columns):
        prix_prem.append(Portefeuille[i].iloc[0])

      for i in range(0,len(prix_prem)):
        nbr.append((x[i]*nominal)/prix_prem[i])

      evol=[]

      for i in range(0,len(list(Portefeuille.columns))):
        evol.append(Portefeuille[actif[i]]*nbr[i])

      Evolution=pd.concat(evol,axis=1)
      Evolution.dropna(inplace=True)
      Evolution_finale=pd.DataFrame()
      Evolution_finale['Price']=Evolution.sum(axis=1)

      Evolution_finale['Rendement_Cumul']=(1+Evolution_finale['Price'].pct_change()).cumprod()

      MSI=MSI.loc[date_backtest:date_finale]
      MSI['Rendement_Cumul']=(1+MSI['Instrument'].pct_change()).cumprod()

      concat=pd.concat(  [ MSI['Rendement_Cumul'],Evolution_finale['Rendement_Cumul']  ] ,axis=1)
      concat.columns=['Portefeuille','Benchmark']

      concat['Portefeuille']=concat['Portefeuille']*100
      concat['Benchmark']=concat['Benchmark']*100

      concat['Portefeuille'].iloc[0]=100
      concat['Benchmark'].iloc[0]=100

      rend[niveau]=(concat['Portefeuille']-concat['Benchmark']).mean()


   
    return list(rend.keys())[np.array(list(rend.values())).argmax()]



  def OPCVM_FINALE(self,actif,date_backtest,date_fin_data,periode,cours_cible,taux,MSI,niveau,nominal,imin,imax):

    #nominal=float(input('Nominal ? \n '))
    rep='1'
    if rep == '1':
      repp='2'
      if repp=='1':
        niveau=float(input('Niveau ? \n'))
        x=self.OPCVM_MAROC(actif,date_backtest,periode,cours_cible,nominal,niveau,taux)
        self.Backtest(actif,nominal,x,date_backtest,date_fin_data,MSI)
      if repp=='2':
        a=imin
        b=imax
        niveau=self.Monte_Carlo(nominal,actif,periode,date_backtest,date_fin_data,cours_cible,taux,a,b,MSI)
        x=self.OPCVM_MAROC(actif,date_backtest,periode,cours_cible,nominal,niveau,taux)
        self.Backtest(actif,nominal,x,date_backtest,date_fin_data,MSI)
        print('\n')
        print('On a travaillé avec un niveau de : {}'.format(niveau))
        print('\n')
        print('Portefeuille : \n')
        print(x)
        print('\n')
        print('Somme : {}'.format(x.sum()))
        data12 = {'--------':'On a travaillé avec un niveau de : {}'.format(niveau),
                  'Portefeuille : ':x,
                  'Somme : ':x.sum()
        }
        df12 = pd.DataFrame(data12)
        return df12

    if rep == "2":
        x=self.OPCVM_CHOIX(nominal,actif,periode,date_backtest,cours_cible,taux)
        self.Backtest(actif,nominal,x,date_backtest,date_fin_data,MSI)













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

def getCovMat(lst1,dated,datef,plot=False):
  a=Portefeuille(data_names)
  return a.Covariance_Matrice(lst1,dated,datef,plot=False)

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

# def getStratCoursCible(nb1,nb2,nb3,dated,datef):
#   a=Construct(data_names)
#   Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
#   d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
#     'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
#   return a.Strat(d,dated,datef,Cours_cible,nb1,nb2,nb3)

# def getNivCost(option,nb1,nb2,nb3,nb4,dbackt):
#   a=Construct(data_names)
#   Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
#   d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
#     'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
#   if option=="niv":
#     return a.OPCVM_MAROC(d,dbackt,nb1,Cours_cible,nb2,nb3,nb4)
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

def getMonteCarlo(datef,dateback,periode,nominal,niveau,taux,imin,imax):
  a=Construct(data_names)
  Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
  d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie',
    'Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
  return a.OPCVM_FINALE(d,dateback,datef,periode,Cours_cible,taux,MSI,niveau,nominal,imin,imax)