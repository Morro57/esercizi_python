"""### 2) Media voti di N studenti  
1.Crea in modo statico un dizionario di N studenti.<br>
Ogni elemento del dizionario contiene come chiave il nome dello studente e come valore una lista di tre tuple, cioè i voti (scritto,orale) in [Matematica, Fisica e Chimica].<br>
2.Il programma chiede all'utente di inserire il nome di uno studente che viene passato ad una funzione che deve restituire una tupla con (media_scritti,media_orali,media_totale).

"""

# Esempio di struttura dati su cui deve lavorare la funzione
voti={'Mario':[(7,8),(6,8),(9,10)],'Pietro':[(7,7),(6,5),(9,8)],"Cristian":[(6,8),(4,10),(6,4)]}

def cercaStudente(voti,studInp):
    controllo= False
    cont_scritti=0
    media_scritti= 0
    cont_orali=0
    media_orali= 0
    cont_totale=0
    media_totale=0
    for nome,materie in voti.items():
        if(nome == studInp):
            controllo = True
            for vScritto,vOrale in materie:
                media_totale+=vScritto+vOrale
                cont_totale+=2

                media_orali+=vOrale
                cont_orali+=1

                media_scritti+=vScritto
                cont_scritti+=1
                #print(vScritto,vOrale)
            media_totale/=cont_totale
            media_scritti/=cont_scritti
            media_orali/=cont_orali
                

    if(controllo==False):
        print("Studente non presente nella lista.")
    else:
        return(media_scritti,media_orali,media_totale)

def inputAlunno():
    alunno=input("Inserisci l'alunno da visualizzare: ")
    if(len(alunno)< 2):
        print("Errore,digitazione errata.")
    else:
        return alunno    

alunno = inputAlunno()
print(cercaStudente(voti,alunno))
while True:

    scelta=int(input("Vuoi cercare un altro studente?(1=si, 2=no): "))
    if(scelta<1 or scelta>2):
        print("Errore, digitazione errata.")
    elif(scelta==2):
        print("Programma terminato.")
        break
    else:
        alunno = inputAlunno()
        print(cercaStudente(voti,alunno))
            
        
    


