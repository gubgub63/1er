import csv
#Def Fonction 
def lireCSV(fichierCSV):
    liste_dicos=[]
    with open(fichierCSV, newline='') as csvfile:
        my_reader = csv.DictReader(csvfile, delimiter=',')
        for row in my_reader:
            liste_dicos.append(dict(row)) # transforme chaque ligne en dictionnaire
    return liste_dicos


def join(ListeCmd,Listeclients) :
    liste=[]
    for i in ListeCmd :
        dico={}
        for a,b in i.items() :
            dico[a]=b
        for y in Listeclients :
            if i['n_client']==y['n_client'] :
                for c,d in y.items() :
                     dico[c]=d
        liste.append(dico)
    return liste






#Programme principale 

a=lireCSV('commandes.csv')
b=lireCSV('clients.csv')
#print(join(a,b))
liste=join(a,b)
clients=[[client['nom']] for client in liste if float(client['Montant en euro'])>300 and client['ville']=='Bordeaux']
print(clients)
