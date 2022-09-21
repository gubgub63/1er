    #Projet deviner un nombre

#Bibliotèque

from random import*

#définition des fonctions

#Fonction qui retourne code secret
def code_secret():
    '''
    Fonction qui créer un nombre aléatoire (en appelant la fonction random) ce nombre comprend des chiffres allant de 1 à 6 
    Le code secret est stocké dans une liste , qui elle se créer sur une boucle de 4 , qui ajoute à chaque tour un nombre aléatoire à la liste (au code)
    La foncion retourne le code secret 
    '''
    code=[]
    for i in range(4):
        code.append(randint(1,6))
    return code

#Fonction qui retourne la proposition du nombre
def proposition():
    '''
    Foncion qui demande au joueur de saisir un nombre (une proposition)
    Cette proposition est ajoutée à une liste en bouclant sur la proposition du joueur
    La fonction retourne la proposition du joueur 
    '''
    essai=input("Saisir un nombre a 4 chiffres: ")
    L1=[]
    for i in essai:
        L1.append(int(i))
    return L1

#fonctions qui retourne le nombre bien ou mal placés
def position_correcte(L1,code):
    '''
    Fonction qui vérifie la proposition du joueur par rapport au code secret 
    Elle vérifie en premier si la position d'un des chiffres est bien placé , pour cela elle boucle sur une valeur i allant de 1 a 4 puis elle verifie si la position i de la proposition est égale a la position i du code secret  ,
    une liste est créée pour permettre dans un deuxième temps de ne pas faire buger le système lorsque qu'il y a des doubles 
    Pour finir la fonction boucle encore sur la position i de la proposition et vérifie si celle-la est dans le code ET si la position i de la proposition n'est pas dans les listes créées plus tôt (cela permet de ne pas réaficher mal placés si le nombre l'est déja)
    La fonction retourne de nombre :
    -en premier le nombre de bien placés 
    -puis le nombre de mal placés 
    '''
    correct=0
    incorrect=0
    liste=L1[:]
    code1=code[:]
    for i in range(4):
        if L1[i]==code[i]:
            correct+=1
            liste[i]=-2
            code1[i]=-1
    for i in range(4):
        if (L1[i]in code1):
            incorrect+=1
            indice=code1.index(L1[i])
            code1[indice]=-9
    return correct,incorrect

#Fonction qui retourne les niveux de jeu
def niveau_de_jeu():
    '''
    Fonction qui demande à l'utilisateur quel(s) niveau(x) de jeux il souhaiterait 
    En fonction de niveau de jeux choisis une variable (essai) va prendre une valeur entre 12 , 8 et 6 , cette valeur est retournés a la fin de la fonction pour être réutiliser plus tard dans le programme principale 
    La fonction vérifie aussi si le niveaux choisis est correct (si il ne dépasse 3 ) , si le niveau choisi n'existe pas l'utilisateur est appelé a saisir un niveau valide 
    '''
    nombres_essai=int(0)
    niveau=int(input("Saisir un niveau de jeu entre 1, 2 et 3 :"))
    while niveau >3:
        niveau=int(input("Saisir un niveau valide : "))

    if niveau==1:
        nombres_essai+=12
    elif niveau==2:
        nombres_essai+=10
    elif niveau==3 :
        nombres_essai+=8
        
    return nombres_essai

#Fonction qui retoune le nombre de joueur
def nombre_joueurs():
    '''
    Fonction qui demande à l'utilisateur le nombre de joueur 
    Le nombre de joueur est stocké dans une variable qui sera retourné à la fin de la fonction et utilisé plus tard dans le programme principale 
    '''
    nb_joueur=int(input("Saisir le nombre de joueur entre 1 et 2: "))
    while nb_joueur!=1 and nb_joueur!=2:
        nb_joueur=int(input("Saisir le nombre de joueur: "))
    return nb_joueur

#Fonction du jeu à 2 joueurs
def jeu_a_deux_joueurs():
    '''
    Fonction qui est appelée dans le programme principale seulement si il y a 2 joueurs 
    Elle reprend les mêmes principes que la fonction proposition (détaillée plus haut)
    '''
    essai=input("Saisir un nombre a 4 chiffres: ")
    L1=[]
    for i in essai:
        L1.append(int(i))
    return L1
    


#Programme principal
print("Bienvenue dans le jeu du devine le nombre !")
print("Le jeu consiste à trouver un nombre secret avec un nombre d'essais défini en fonction du niveau choisi")
print("Niveau 1 = 12 essais")
print("Niveau 2 = 10 essais")
print("Niveau 3 = 8 essais")
print("Le nombre secret est composé de 4 chiffres compris entre 1 et 6 ")
joueurs=nombre_joueurs()    
niveau=niveau_de_jeu()
code=code_secret()



print("Le jeu commence vous avez ",niveau,"essais")
fini=False
while not fini :
    if joueurs==2:
        L1=proposition()
        L2=jeu_a_deux_joueurs()
        
        bonne_place,mauvaise_place=position_correcte(L1,code)
        
        bonne_place1,mauvaise_place1=position_correcte(L2,code)
        
        if position_correcte(L1,code)!=(4,0)and position_correcte(L2,code) !=(4,0):
            print("Joueur 1 vous avez ",bonne_place ,"nombres bien placés",mauvaise_place,"nombres mal placés")
            print("Joueur 2 vous avez ",bonne_place1 ,"nombres bien placés",mauvaise_place1,"nombres mal placés")
            niveau-=1
            print("Il vous reste ", niveau ,"essais")
            
                    
        elif position_correcte(L1,code)==(4,0) or position_correcte(L2,code) ==(4,0):
            fini=True
        
    elif joueurs==1:
        L1=proposition()
        bonne_place,mauvaise_place=position_correcte(L1,code)
        
        if position_correcte(L1,code)!=(4,0):
            print(bonne_place ,"nombres bien placés",mauvaise_place,"nombres mal placés")
            niveau-=1
            print("Il vous reste ", niveau ,"essais")
            
        elif position_correcte(L1,code)==(4,0):
            fini=True

    if niveau<=0 :
        fini=True
        
if joueurs==1:
    if position_correcte(L1,code)==(4,0):
        print("Vous avez gagné avec ",niveau,"essais restant !")
        
    else :
      print(" Le nombre d'essais est dépassé, vous avez perdu.")
      
elif joueurs==2 :
    if position_correcte(L1,code)==(4,0) :
        print("Bravo ,joueur 1 vous avez gagné avec",niveau,"essais restant !")
        
    elif position_correcte(L2,code)==(4,0) :
        print("Bravo , joueur 2 vous avez gagné avec",niveau,"essais restant !")
    elif position_correcte(L2,code) and position_correcte(L1,code)!=(4,0):
        print("Joueur 1 et 2 vous avez perdu :( ")
        










        
        
