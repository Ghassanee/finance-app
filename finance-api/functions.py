import numpy as np
import pandas as pd
import BVCscrap as load
from numpy.linalg import inv
import cvxpy as cv 
     

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
        return scatter_matrix(Calcul_Rendement_Actifs(actif, 'Quotidien', date_debut,
                       date_fin, False), hist_kwds={'bins': 600}, alpha=0.8, figsize=(17, 9))


def Portefeuille_Risk_Minimum(actif:list,cours_cible,date_debut,date_fin):

    # Portefeuille qui nous garentit le risque minimum ( sans aucune contrainte )
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # a.Portefeuille_Risk_Minimum(d,Cours_cible,'2020-01-01','2022-05-18')
    
    V= Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    a=np.dot(V_inv,e)
    p=np.dot(np.dot(e.T,V_inv),e)

    x=a/p
    
    print('Le portefeuille qui garentit le minimum de risque :  ')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} %' .format(actif[i],round(x[i]*100,3)) )
    
    print('\n')
    print('On a bien une somme de :  ')
    print('{}  %'.format(100*(a/p).sum()))

    print('\n')
    print('Le niveau de risque minimum :  ')
    print("{} % ".format(100*np.dot(np.dot((a/p).T,V),(a/p).T)**0.5))
    print('\n')

    Vecteur_Esper=[]
    
    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)


    Vecteur_Esper=np.array(Vecteur_Esper)
    print('Le Rendement Espéré de votre Portefeuille :')
    print('{}  %'.format(100*np.dot(Vecteur_Esper,(a/p))))


def Portefeuille_Risk_Minim_Esper(actif:list,cours_cible,E0,date_debut,date_fin):

    # Portefeuille qui nous garentit le rendement cible E0 en prenant le risque minimum ( Le Rendement espéré est la seule contrainte posée : E0 )
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # a.Portefeuille_Risk_Minim_Esper(d,Cours_cible,0.12,'2020-01-01','2022-05-18')

    
    V=Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

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

    print('Le Portefeuille qui vous garentit le risque minimum à votre Espérance espéré : ')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} % '.format(actif[i],o[i]*100))
    print('\n')
    
    print('On a bien ') 
    print( '{}  %' .format(100*(1/D)*(a+b).sum() ) )
    print('\n')
    
    print('Votre Niveau de Risque ')
    print('{} %' .format(100*np.dot(np.dot(((1/D)*(a+b)).T,V),((1/D)*(a+b)).T)**0.5 )    )
    print('\n')

    print('Votre Rendement est bien :')
    print("{} %" .format(100*np.dot(o,Vecteur_Esper) )  )


def Return_Risque_Frontière_Effic(actif:list,cours_cible,E0,date_debut,date_fin):

    # Fonction qui nous retourne le risque minimum pour une Espérance de Rendement donnée ( Pas de boutton dans les interfaces graphique )
    
    V=Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

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


def Portefeuille_Esper_Minimum(actif:list,cours_cible,date_debut,date_fin):

    # Fonction qui nous retourne le rendement maximum pour un risque donné ( Pas de boutton dans les interfaces graphique )

    V= Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    a=np.dot(V_inv,e)
    p=np.dot(np.dot(e.T,V_inv),e)

    x=a/p
    

    Vecteur_Esper=[]
    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
    
    return np.dot(Vecteur_Esper,(a/p))


def Plot_Front_Effic(actif:list,cours_cible, date_debut,date_fin):

    # Visualisation de la frontière efficiente pour un niveau de rendement espéré donné ( Fonction intégrée dans nos interfaces graphiques )
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # a.Plot_Front_Effic(d,Cours_cible,'2020-01-01','2022-05-18')


    risque_minim= Return_Risque_Frontière_Effic( actif, cours_cible,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin) , date_debut, date_fin )

    risque=[risque_minim,Return_Risque_Frontière_Effic( actif, cours_cible,  Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.01 ,date_debut,date_fin ),
            Return_Risque_Frontière_Effic(actif,cours_cible,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.02 , date_debut , date_fin),
            Return_Risque_Frontière_Effic(actif,cours_cible,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.03, date_debut , date_fin) ,
            Return_Risque_Frontière_Effic(actif,cours_cible,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut , date_fin )+0.04,  date_debut  ,  date_fin ),
            Return_Risque_Frontière_Effic(actif,cours_cible,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut , date_fin )+0.05 , date_debut , date_fin  ),
            Return_Risque_Frontière_Effic(actif,cours_cible,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut, date_fin)+0.06, date_debut , date_fin )  ]

    rendement=[
               Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)
              ,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.01
               ,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.02
               ,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.03
               ,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.04
               ,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.05
               ,Portefeuille_Esper_Minimum(actif,cours_cible,date_debut,date_fin)+0.06  ]

    plt.figure(figsize=(17,9))
    plt.plot(risque,rendement,'*-',c='r')
    plt.xlabel('Risque ')
    plt.ylabel('Rendement Espéré ')
    plt.title('La Frontière Efficiente des {} Actifs : {} Entre la date : {} et la date : {} '.format(len(actif),actif,date_debut,date_fin))


def Portefeuille_Tangeant(actif:list,cours_cible,E0,Rf,date_debut,date_fin) :

    # Portefeuille Tangeant ( Seul le rendement est la contrainte )
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # a.Portefeuille_Tangeant(d,Cours_cible,0.21,0.05,'2020-01-01','2022-05-18')


    V=Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

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

    print('Rendement de votre Portefeuille Risqué :')
    rendement = np.dot(pend.T,Vecteur_Esper)
    print('{} '.format(rendement))
    print('\n')

    print('Ponderation de l actif Risqué :')
    print('\n')
    for i in range(0,20):
      print('{} : {} '.format(actif[i],pend[i]))
  
    print('\n')


    print('Ponderation de l actif sans Risque :')
    pp=1-(np.dot(pend.T,e))
    print(pp)
    print('\n')

    print('Somme des Ponderations de votre Portefeuille Risqué :')
    print(pend.sum())
    print('\n')
    
    print('On a bien La somme des Ponderations  :')
    print(pp+pend.sum())
    print('\n')

    print('Rendement Espéré Total de votre Portefeuille :')
    rend_portefeuille=pp*Rf+rendement
    print("{}  ".format(rend_portefeuille))
    print('\n')
    
    print('Risque :')
    risque = (np.dot(np.dot(pend,V),pend)**0.5)
    print(risque)
    print('\n')


def Portefeuille_Minim_Risk_Limite(actif:list,cours_cible,u,limite,date_debut,date_fin):

    # Portefeuille à risque minimum 
    # Contraintes : Pas de Vente à Découvert + Somme des actifs choisis égale à une certaine limite
    # u : np.array() dépend du choix de l utilisateur ( prend que des 0 et 1 )
    
    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # u=np.array([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])
    # a.Portefeuille_Minim_Risk_Limite(d,Cours_cible,u,0.4,'2021-01-01','2022-05-18') 



    V=Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    

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

  
    print('Le Portefeuille qui Vous Garantit Le Risque Minimum est :')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} '.format(actif[i],c[i]))
    print('\n')

    print('Le Risque Minimum est : ')
    print(np.dot(np.dot(c,V),c)**0.5)
    print('\n')

    print('On a Bien la somme des Penderation est : ')
    print(c.sum())
    print('\n')

    print('La contrainte de Pondération est bien respectée :')
    print(np.dot(c,u))
    print('\n')

    print('Votre Rendement dans Ce cas : ')
    print(np.dot(c,Vecteur_Esper))
    print('\n')

    print('Pas de Vente à Découvert  ! ! ! ')


def Portefeuille_Minim_Risk_Limite_Esper(actif:list,cours_cible,u,limite,E0,date_debut,date_fin):
    
    # Portefeuille à risque minimum 
    # Contraintes : Pas de Vente à Découvert + Somme des actifs choisis égale à une certaine limite + Espérance de rendement = E0 ( donné par l utilisateur )
    # u : np.array() dépend du choix de l utilisateur ( prend que des 0 et 1 )

    # a=Portefeuille(data_names)
    # Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
    # d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']
    # u=np.array([1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
    # a.Portefeuille_Minim_Risk_Limite_Esper(d,Cours_cible,u,0.1,0.5,'2021-01-01','2022-05-18')


    V=Covariance_Matrice(actif,date_debut,date_fin,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    

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

    #print(prob.status)

    if prob.status == 'infeasible':
      print('Solution ne converge pas ! Contraintes Contradictoires  !!!! ')
      return 

    c= x.value

    print('Le Portefeuille adéquat à votre Rendement est : ')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} '.format(actif[i],c[i]))
    print('\n')

    print('Votre Rendement Espéré est Bien : ')
    print(np.dot(c,Vecteur_Esper))
    print('\n')

    print('La somme des Pondérations est : ')
    print(c.sum())
    print('\n')

    print('Le Risque de Votre Portefeuille est  : ')
    print(np.dot(np.dot(c,V),c)**0.5)
    print('\n')

    print('La Contrainte De pondérations est Bien Respectée ') 
    print(np.dot(c,u).sum())
    print('\n')

    print('Pas De Vente à Découvert !!!') 


def Portefeuille_Constitution(actif:list,cours_cible,window,Nominal,Niveau):
    
    # Fonction qui nous donne le portefeuille optimal ( avec une contraine de liquidité )
    # Pas de Vente à Découvert 
    # On calcule la moyenne du volume observé dans un intervale de taille : window en commençant avec la dernière date téléchargée dans notre dataset .

     

    V=Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))
    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
  
    Contr=[]

    print('Les Niveaux à ne pas dépacer ')
    print('\n')
    for j in range(0,len(actif)) :
      Contr.append( ( data_names[actif[j]].tail(window)['VOLUME'].mean()* Niveau  )/ Nominal )

    for k in range(0,len(actif)):
      print('{}  :  {}  '.format(actif[k],Contr[k]))
  
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
      return 
    
    print('\n')
    print('Le Portefeuille qui vous garantit le risque Minimum est :')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} '.format(actif[i],c[i]))
    print('\n')

    print('Le Risque Minimum est : ')
    print(np.dot(np.dot(c,V),c)**0.5)
    print('\n')

    print('On a Bien la somme des Penderation est : ')
    print(c.sum())
    print('\n')

    print('Pas de Vente à Découvert  ! ! ! ')

    return c 


def Strat(actif:list,date_debut_data:str,date_fin_data:str,cours_cible,Nominal,Niveau,window):

    # Stratégie pour repondérer notre Portefeuille si un de nos actifs détenu atteint son cours Cible ( Atteint son Espérance de Rendement )
    # La stratégie marche entre les deux dates : date_debut_data et date_end_data 

    c=Portefeuille_Constitution(actif,cours_cible,window,Nominal,Niveau)
    mm=[]

    for i in range(0,len(actif)):
      mm.append(data_names[actif[i]].loc[date_debut_data:date_fin_data]['COURS_CLOTURE'])
    

    for i in range(0,len(mm)):
      Portefeuillee_Penderation = pd.concat(mm,axis=1)
    
    Portefeuillee_Penderation.columns = actif

    for i in range(0,len(c)):
      Portefeuillee_Penderation[actif[i]]=Portefeuillee_Penderation[actif[i]]*c[i]

    Portefeuillee_Penderation.dropna(axis=0,inplace=True)

    #print(Portefeuillee_Penderation)

    m=[]

    for i in range(0,len(actif)):
      m.append(data_names[actif[i]].loc[date_debut_data:date_fin_data]['COURS_CLOTURE'])
    
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


def Portefeuille_Constitution_OPCVM(actif:list,date_backtest,periode_volume,cours_cible,Nominal,Niveau,rr):
    

    V=Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
  

    Contr=[]

    print('Les Niveaux à ne pas dépacer ')
    print('\n')
    for j in range(0,len(actif)) :
      Contr.append( ( data_names[actif[j]].loc[:date_backtest].tail(periode_volume)['VOLUME'].mean()* Niveau  )/ Nominal )
    
    so=np.array(Contr).sum()
    #print('so : {}'.format(so))
    

    if so > 1 and so <= 1.31 :
      u= 1.37-np.array(Contr).sum() 
      for i in range(0,len(Contr)):
        Contr[i]=Contr[i]+u*( Contr[i]/np.array(Contr).sum() )

      #print('u : {}'.format(u))

    print('\n')
    for i in range(0,len(Contr)):
      print('{} : {}'.format(actif[i],Contr[i]))
   

    print('\n')
    print('La Somme des contraintes : {} '.format(np.array(Contr).sum()))
    print('\n')

    

    
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
  
    print('\n')
    print('Le Portefeuille qui vous garantit le risque Minimum est :')
    print('\n')
    for i in range(0,len(actif)):
      print('{} : {} '.format(actif[i],c[i]))
    print('\n')
    
    print('Somme des 4 premières valeurs : {}'.format(c[0]+c[1]+c[2]+c[3]))
    print('\n')

    if 'Attijari' in actif :
      print('On a bien la Ponderation de Attijari  = {}  <  {} '.format(c[actif.index('Attijari')],0.20))
      print('\n')

    if 'Itissalat' in actif :
      print('On a bien la Ponderation de Itissalat  = {}  <  {}'.format(c[actif.index('Itissalat')],0.15))
      print('\n')

    

    print('Le Risque Minimum est : ')
    print(np.dot(np.dot(c,V),c)**0.5)
    mp=np.dot(np.dot(c,V),c)**0.5
    print('\n')

    print('On a Bien la somme des Penderation est : ')
    print(c.sum())
    print('\n')

    print('Pas de Vente à Découvert  ! ! ! ')
    print('\n')

    indice=[]
    f=[]

    for i in range(0,len(c)):
      if c[i]>0.1:
        print('l actif {} a une ponderation de {} '.format(actif[i],c[i]))
        f.append(c[i])
        indice.append(i)
    
    print('\n')
    print('La somme des titres qui dépace 0.1 est {}'.format(np.array(f).sum()))
    print('\n')
    if np.array(f).sum() <= 0.45 :
      return c

    if np.array(f).sum() > 0.45 :
      print('Il nous reste {} - 0.45 = {} à éliminer '.format(np.array(f).sum(),np.array(f).sum()-0.45))

      print('\n')
     
      
      print('Elimination proportionelle :')
      print('\n')

        
      for i in range(0, len(f)):
        print('Le Titre {} va perdre {} de {}'.format(actif[indice[i]],f[i]/np.array(f).sum(),np.array(f).sum()-0.45))
          
      for k in indice : 
        c[k] = c[k]-((np.array(f).sum()-0.45)*(f[indice.index(k)]/np.array(f).sum()))

      print('\n')
      for k in range(0,len(c)):
        if k in indice :
          print('{} : {}  <--------------- '.format(actif[k],c[k]))
        else :
          print('{} : {} '.format(actif[k],c[k]))

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
      
        
      return c
 

def Portefeuille_Constitution_OPCVM_test(actif:list,date_backtest,periode_volume,cours_cible,Nominal,Niveau,rr):
    
     

    V=Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)
  

    Contr=[]

    print('Les Niveaux à ne pas dépacer ')
    print('\n')
    for j in range(0,len(actif)) :
      Contr.append( ( data_names[actif[j]].loc[:date_backtest].tail(periode_volume)['VOLUME'].mean()* Niveau  )/ Nominal )
    

    for k in range(0,len(actif)):
      print('{}  :  {}  '.format(actif[k],Contr[k]))

    print('\n')
    
   
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
        print('Attijari est suponderé de {}'.format(rest))
        print('\n')
        print('Le reste : {} : répartition proportionelle '.format(rest))
        print('\n')
        for im in range(indice_attijari[0]+1,len(Contr)):
          Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
        for k in range(0,len(Contr)):
          print('{}  :  {}  '.format(actif[k],Contr[k]))
      #print('Somme : {}'.format(np.array(Contr).sum()))
      else :
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
        for im in range(indice_Itissalat[0]+1,len(Contr)):
          Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
        print('\n')
        for k in range(0,len(Contr)):
          print('{}  :  {}  '.format(actif[k],Contr[k]))
      else :
        print('\n')
        print('La ponderation de Itissalat : {} < 0.15'.format(Contr[actif.index('Itissalat')]))
        print('\n')
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
        print('La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum()))
        re=ss-0.45
        print('\n')
        print('Le reste : {} = {} - 0.45 répartition proportionelle '.format(re,ss))
        print('\n')
        
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

      
      
      for k in range(0,len(Contr)):
          print('{}  :  {}  '.format(actif[k],Contr[k]))
      
      print('\n')
      
     
      #print('La somme est {}'.format(np.array(Contr).sum()))
      
      sm=np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])
      
      if sm <=0.45:
        print('La somme des 4 premières valeurs {} <= 0.45'.format(sm))
      else :
        print('La somme des 4 premières valeurs {} > 0.45'.format(sm))
        print('Répartition proportionnelle de {} - 0.45 = {}'.format(sm,sm-0.45))
        for ik in range(0,4):
          Contr[ik]=Contr[ik]-(sm-0.45)*(Contr[ik]/np.array(Contr[:4]).sum())
        for ikk in range(5,len(Contr)):
          Contr[ikk]=Contr[ikk]+(sm-0.45)/5
        

        print('\n')
        for k in range(0,len(Contr)):
          print('{}  :  {}  '.format(actif[k],Contr[k]))
        print('\n')
        print('On a bien la somme des 4 premières valeurs {} <= 0.45'.format(np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])))
      
      print('\n')
      if np.array(Contr).sum()>1 :
        ed=np.array(Contr).sum()-1
        for i in range(0,len(Contr)):
          Contr[i]=Contr[i]-ed*(Contr[i]/np.array(Contr).sum())
      print('la somme : {}'.format(np.array(Contr).sum()))

      return np.array(Contr)

  
def OPCVM_MAROC(actif,date_backtest,periode,Cours_cible,nominal,niveau,taux):
    
     
    V=Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((Cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    Contr=[]

    for j in range(0,len(actif)) :
      Contr.append( ( data_names[actif[j]].tail(periode)['VOLUME'].mean()* niveau  )/ nominal )
    
    so=np.array(Contr).sum()
    


    if so <= 1.17:
      return Portefeuille_Constitution_OPCVM_test(actif,date_backtest,periode,Cours_cible,nominal,niveau,taux)
    
    if so > 1.17  :
      return Portefeuille_Constitution_OPCVM(actif,date_backtest,periode,Cours_cible,nominal,niveau,taux)


def Backtest(actif:str,nominal,x,date_backtest,date_fin_data,MSI):
    
    prix=[]
    prix_prem=[]
    nbr=[]
    Portefeuille=pd.DataFrame()

    nominal=nominal*np.array(x).sum()
    print('\n')

    print('Nominal du Backtest : {} '.format(nominal))
    print('\n')
    print('\n')
    for i in range(0,len(actif)) :
      prix.append(data_names[actif[i]]['COURS_CLOTURE'].loc[date_backtest:])

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

    V=Covariance_Matrice(actif,False)
    print('\n')
    #print('Risque Espéré de notre Portefeuille : {}'.format(np.dot(np.dot(x,V),x)**0.5))
    print('\n')
    print('Risque Observé de Portefeuille : {} '.format((Evolution_finale['Price'].pct_change()).std()))
    print('Risque Observé de Benchmark : {} '.format((MSI['Instrument'].loc[date_backtest:date_fin_data].pct_change()).std()))
    print('\n')
    print('\n')


def OPCVM_CHOIX(nominal,actif,periode,date_backtest,cours_cible,taux):

    niveau={}

    for i in actif : 
      niveau[i]=float(input('Niveau de liquidité choisi pour : {}  ? \n'.format(i)))

        
     
    V=Covariance_Matrice(actif,False)
    V_inv=inv(V)
    e=np.ones(len(actif))

    Vecteur_Esper=[]

    for i in range(0,len(actif)):
      Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

    Vecteur_Esper=np.array(Vecteur_Esper)

    Contr=[]

    for j in range(0,len(actif)) :
      Contr.append( ( data_names[actif[j]].tail(periode)['VOLUME'].mean()* niveau[actif[j]]  )/ nominal )
    
    so=np.array(Contr).sum()

    if so <= 1.17:
      
       

      V=Covariance_Matrice(actif,False)
      V_inv=inv(V)
      e=np.ones(len(actif))

      Vecteur_Esper=[]

      for i in range(0,len(actif)):
        Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

      Vecteur_Esper=np.array(Vecteur_Esper)
  

      Contr=[]

      print('Les Niveaux à ne pas dépacer ')
      print('\n')
      for j in range(0,len(actif)) :
        Contr.append( ( data_names[actif[j]].loc[:date_backtest].tail(periode)['VOLUME'].mean()* niveau[actif[j]]  )/ nominal )
    

      for k in range(0,len(actif)):
        print('{}  :  {}  '.format(actif[k],Contr[k]))

      print('\n')
    
   
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
          print('Attijari est suponderé de {}'.format(rest))
          print('\n')
          print('Le reste : {} : répartition proportionelle '.format(rest))
          print('\n')
          for im in range(indice_attijari[0]+1,len(Contr)):
            Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
          for k in range(0,len(Contr)):
            print('{}  :  {}  '.format(actif[k],Contr[k]))
        #print('Somme : {}'.format(np.array(Contr).sum()))
        else :
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
          for im in range(indice_Itissalat[0]+1,len(Contr)):
            Contr[im]=Contr[im]+rest*(Contr[im]/np.array(Contr).sum())
          print('\n')
          for k in range(0,len(Contr)):
            print('{}  :  {}  '.format(actif[k],Contr[k]))
        else :
          print('\n')
          print('La ponderation de Itissalat : {} < 0.15'.format(Contr[actif.index('Itissalat')]))
          print('\n')
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
          print('La somme des Titres qui dépacent 0.1 : {}'.format(np.array(f).sum()))
          re=ss-0.45
          print('\n')
          print('Le reste : {} = {} - 0.45 répartition proportionelle '.format(re,ss))
          print('\n')
        
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

      
      
        for k in range(0,len(Contr)):
           print('{}  :  {}  '.format(actif[k],Contr[k]))
      
        print('\n')
      
     
        #print('La somme est {}'.format(np.array(Contr).sum()))
      
        sm=np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])
      
        if sm <=0.45:
          print('La somme des 4 premières valeurs {} <= 0.45'.format(sm))
        else :
          print('La somme des 4 premières valeurs {} > 0.45'.format(sm))
          print('Répartition proportionnelle de {} - 0.45 = {}'.format(sm,sm-0.45))
          for ik in range(0,4):
            Contr[ik]=Contr[ik]-(sm-0.45)*(Contr[ik]/np.array(Contr[:4]).sum())
          for ikk in range(5,len(Contr)):
            Contr[ikk]=Contr[ikk]+(sm-0.45)/5
        

          print('\n')
          for k in range(0,len(Contr)):
            print('{}  :  {}  '.format(actif[k],Contr[k]))
          print('\n')
          print('On a bien la somme des 4 premières valeurs {} <= 0.45'.format(np.array(Contr[0])+np.array(Contr[1])+np.array(Contr[2])+np.array(Contr[3])))
      
        print('\n')
        if np.array(Contr).sum()>1 :
          ed=np.array(Contr).sum()-1
          for i in range(0,len(Contr)):
            Contr[i]=Contr[i]-ed*(Contr[i]/np.array(Contr).sum())
        print('la somme : {}'.format(np.array(Contr).sum()))

        return np.array(Contr)

      

        
    
    if so > 1.17  :
      
       
      V=Covariance_Matrice(actif,False)
      V_inv=inv(V)
      e=np.ones(len(actif))

      Vecteur_Esper=[]

      for i in range(0,len(actif)):
        Vecteur_Esper.append((cours_cible[i]/data_names[actif[i]]['COURS_CLOTURE'].loc[:date_backtest].iloc[-1])-1)

      Vecteur_Esper=np.array(Vecteur_Esper)
  

      Contr=[]

      print('Les Niveaux à ne pas dépacer ')
      print('\n')
      for j in range(0,len(actif)) :
        Contr.append( ( data_names[actif[j]].loc[:date_backtest].tail(periode)['VOLUME'].mean()* niveau[actif[j]]  )/ nominal )
    
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
   

      print('\n')
      print('La Somme des contraintes : {} '.format(np.array(Contr).sum()))
      print('\n')

    

    
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
        if nominal >= 20000000 and nominal < 50000000:
          return Portefeuille_Constitution_OPCVM(actif,date_backtest,periode,Cours_cible,nominal,0.3,taux)
        if nominal >= 50000000:
          return Portefeuille_Constitution_OPCVM(actif,date_backtest,periode,Cours_cible,nominal,1,taux)
        
  
      print('\n')
      print('Le Portefeuille qui vous garantit le risque Minimum est :')
      print('\n')
      for i in range(0,len(actif)):
        print('{} : {} '.format(actif[i],c[i]))
      print('\n')
    
      print('Somme des 4 premières valeurs : {}'.format(c[0]+c[1]+c[2]+c[3]))
      print('\n')

      if 'Attijari' in actif :
        print('On a bien la Ponderation de Attijari  = {}  <  {} '.format(c[actif.index('Attijari')],0.20))
        print('\n')

      if 'Itissalat' in actif :
        print('On a bien la Ponderation de Itissalat  = {}  <  {}'.format(c[actif.index('Itissalat')],0.15))
        print('\n')

    

      print('Le Risque Minimum est : ')
      print(np.dot(np.dot(c,V),c)**0.5)
      mp=np.dot(np.dot(c,V),c)**0.5
      print('\n')

      print('On a Bien la somme des Penderation est : ')
      print(c.sum())
      print('\n')

      print('Pas de Vente à Découvert  ! ! ! ')
      print('\n')

      indice=[]
      f=[]

      for i in range(0,len(c)):
        if c[i]>0.1:
          print('l actif {} a une ponderation de {} '.format(actif[i],c[i]))
          f.append(c[i])
          indice.append(i)
    
      print('\n')
      print('La somme des titres qui dépace 0.1 est {}'.format(np.array(f).sum()))
      print('\n')
      if np.array(f).sum() <= 0.45 :
        return c

      if np.array(f).sum() > 0.45 :
        print('Il nous reste {} - 0.45 = {} à éliminer '.format(np.array(f).sum(),np.array(f).sum()-0.45))

        print('\n')
     
      
        print('Elimination proportionelle :')
        print('\n')

        
        for i in range(0, len(f)):
          print('Le Titre {} va perdre {} de {}'.format(actif[indice[i]],f[i]/np.array(f).sum(),np.array(f).sum()-0.45))
          
        for k in indice : 
          c[k] = c[k]-((np.array(f).sum()-0.45)*(f[indice.index(k)]/np.array(f).sum()))

        print('\n')
        

        for k in range(0,len(c)):
          if k in indice :
            print('{} : {}  <--------------- '.format(actif[k],c[k]))
          else :
            print('{} : {} '.format(actif[k],c[k]))

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
      
        
        return c
    

def Monte_Carlo(nominal,actif,periode,date_backtest,date_finale,cours_cible,taux,a,b,MSI):
    
    #OPCVM_MAROC(,actif,date_backtest,periode,Cours_cible,nominal,niveau,taux)
    rend={}
    x=[]

    for i in range(0,50):
      niveau=float(np.random.uniform(a,b,1))
      print('Niveau : {}'.format(niveau))
      x=OPCVM_MAROC(actif,date_backtest,periode,cours_cible,nominal,niveau,taux)
          
      prix=[]
      prix_prem=[]
      nbr=[]
      Portefeuille=pd.DataFrame()

      for i in range(0,len(actif)) :
        prix.append(data_names[actif[i]]['COURS_CLOTURE'].loc[date_backtest:date_finale])

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


def OPCVM_FINALE(actif,date_backtest,date_fin_data,periode,cours_cible,taux,MSI):

    nominal=float(input('Nominal ? \n '))
    rep=input('1 : Niveau Constant   2 : Niveau Variable ')
    if rep == '1':
      repp=input('1 : Niveau à Entrer   2 : Monte Carlo  ')
      if repp=='1':
        niveau=float(input('Niveau ? \n'))
        x=OPCVM_MAROC(actif,date_backtest,periode,cours_cible,nominal,niveau,taux)
        Backtest(actif,nominal,x,date_backtest,date_fin_data,MSI)
      if repp=='2':
        a=float(input('intervalle min :'))
        b=float(input('intervalle max :'))
        niveau=Monte_Carlo(nominal,actif,periode,date_backtest,date_fin_data,cours_cible,taux,a,b,MSI)
        x=OPCVM_MAROC(actif,date_backtest,periode,cours_cible,nominal,niveau,taux)
        Backtest(actif,nominal,x,date_backtest,date_fin_data,MSI)
        print('\n')
        print('On a travaillé avec un niveau de : {}'.format(niveau))
        print('\n')
        print('Portefeuille : \n')
        print(x)
        print('\n')
        print('Somme : {}'.format(x.sum()))

    if rep == "2":
        x=OPCVM_CHOIX(nominal,actif,periode,date_backtest,cours_cible,taux)
        Backtest(actif,nominal,x,date_backtest,date_fin_data,MSI)


