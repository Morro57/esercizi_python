"""
### 1) Media voti di uno studente
Supponiamo di dover gestire i voti di uno studente in diverse materie.

Utilizza un dizionario per memorizzare i voti dello studente, come chiave la materia e come valore una tupla con il voto (scritto,orale).

Il programma chiede all'utente di inserire i voti per ciascuna materia e alla fine dell'inserimento calcola la media dei voti (scritti, orali, complessiva)utilizzando una funzione che deve restituire una tupla (media_scritti,media_orali,media_totale).
"""

#Esempio di struttura dati su cui deve lavorare la funzione
voti={'italiano':(7,6),'storia':(5,7),'tpsi':(6,8)}

def metodo (voti):
    while True:
        materia = input("Inserisci la materia da inserire: ")
        if(len(materia) <2):
            print("Errore, digitazione mancante o errata")
        if(materia in voti.keys()):
            print("Errore, materia già registrata.")
        else:
            break
    while True:
        vScritto=int(input(f"Inserisci il voto scritto della materia di {materia}: "))
        if(vScritto<0 or vScritto>10):
            print("Errore, il voto deve essere compreso tra 0 e 10.")
        else: 
            break
    while True:
        vOrale=int(input(f"Inserisci il voto orale della materia di {materia}: "))
        if(vOrale<0 or vOrale>10):
            print("Errore, il voto deve essere compreso tra 0 e 10.")
        else:
            break
    #print(vScritto,vOrale)
    voti [materia] = (vScritto,vOrale)



def calcolaMedie(voti):
    cont_scritti=0
    media_scritti= 0
    cont_orali=0
    media_orali= 0
    cont_totale=0
    media_totale=0

    for materia,tipoVoto in voti.items() :
        #print(tipoVoto,type(tipoVoto))
        vScritto,vOrale=tipoVoto
        media_totale+=vScritto+vOrale
        cont_totale+=2

        media_orali+=vOrale
        cont_orali+=1

        media_scritti+=vScritto
        cont_scritti+=1
    media_totale/=cont_totale
    media_scritti/=cont_scritti
    media_orali/=cont_orali
    return  (media_scritti,media_orali,media_totale)



    
metodo(voti)
while True:
    scelta=int(input("Vuoi inserire altre materie?(1=s , 2=no):"))
    if(scelta<1 or scelta>2):
        print("Errore, digitazione errata.")
    elif(scelta==1):
        metodo(voti)
    else:
        print(calcolaMedie(voti))
        break