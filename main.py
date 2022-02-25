print("")
print("IDENTIFICATION JOUEUR : ")
print("")
def afficher_info_personne(numero_personne, nom, age) :
    print("IDENTIFICATION EN COURS...")
    print("JOUEUR ", numero_personne, nom, "Vous avez ", age, " ans. Bienvenue à vous dans notre base de données ! ")

def info_personnes(numero_personne):

    nom = input("Le joueur " + str(numero_personne) + " est : ")
    age = input("ID :"+ nom + " validé. ENTREZ votre âge : ")
    '''try:
        age_int=int(age)
        if not 1<age_int<100:
            print("Erreur: Vous devez rentrer un nombre entre 1 et 100 pour l'âge")
            return info_personnes(numero_personne)
        return age
    except:
        print("ERREUR : Vous devez rentrer un NOMBRE ici !")
        return info_personnes(numero_personne)
    afficher_info_personne(numero_personne, nom, age)'''
    if int(age) < 18:
        print("Vous êtes mineur ")
    else:
        print("Vous êtes majeur")
    if len(nom) <= 4:
        import random
        a = 1
        b = 0
        parole_bot = random.randint(b, a)
        if parole_bot == 1:
            print("ID:",nom," comporte", len(nom), "caractères. C'est un nom court mais très jolie ! ")
        else:
            print("ID:",nom," comporte", len(nom), "caractères. Tant de simplicité pour faire briller son épée ! ")
    else:
        import random
        a=1
        b = 0
        parole_bot= random.randint(b,a)
        if parole_bot == 1:
            print("ID:",nom," comporte", len(nom), "caractères. C'est un nom assez long mais tout aussi mignon !")
        else :
            print(" ID:",nom," comporte", len(nom), "caractères. Seul les grands Hommes portent des noms aussi longs !")

nb_personnes = input("Quel est le nombre de joueur(s) ?")
if 0<int(nb_personnes) <2:
    print("Soldat, vous serez seul pour cette aventure")
else:
    print("Rien ne vaut de tel qu'une belle équipe de bras cassés! Vous serez ",nb_personnes," cette fois-ci." )
for i in range (int(nb_personnes)):
    info_personnes(i+1)
print()
print("Bonne chance à vous")







