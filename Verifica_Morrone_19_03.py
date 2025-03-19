#suggerimenti per la validazione
#oltre alle funzione len() utilizzare la funzione isinstance()
# per verificare se un oggetto appartiene a una determinata classe.
# Restituisce True se l'oggetto è un'istanza della classe specificata
"""lista = [1,2]
print(isinstance(lista, tuple))
tupla=(2,3)
print(isinstance(tupla, tuple))"""

import random
n=random.randint(1,10)

listaPolizze={}

#P1
def popola():
    listaPolizze["Bianchi Anna"] = [("Auto",(8,9,7),"Premium"),
                                ("Casa",(6,8,7),"Standard"),
                                ("Salute",(7,9,6),"Premium"),
                                ("Viaggi",(8,7,9),"Base")   ]
    listaPolizze["Rossi Marco"] = [("Auto",(7,8,9),"Standard"),
                                ("Casa",(9,8,7),"Premium"),
                                ("Salute",(6,8,7),"Base"),
                                ("Viaggi",(9,6,8),"Standard")   ]

#P2
def aggiungiMe():
    listaPolizze ["Morrone Cristian"]= [("Auto",(6,4,9),"Base"),
                                ("Casa",(6,4,7),"Premium"),
                                ("Salute",(8,4,7),"Base"),
                                ("Viaggi",(9,4,8),"Standard")   ]
    

#P3
def aggiungiPolizza():
    #polizza=[]
    for chiave in listaPolizze.keys():
        listaPolizze[chiave].append(("RC Professionale",(random.randint(1,10),random.randint(1,10),random.randint(1,10)),"Standard"))


#P4
def stampaCliente():
    print("Stampa dati clienti, inserire i dati del cliente che si vuole cercare: ")
    nominativo=input_nominativo()

    if nominativo not in listaPolizze.keys():
        print("Cliente ricercato non esistente o presente nella lista.")
    else:
        print("Cliente: "+nominativo)
        for polizza in listaPolizze[nominativo]:
            tipoPolizza,(copertura,costo,affidabilita),livello =polizza
            
            print(f"Polizza {tipoPolizza}: ") 
            print("Copertura: ",str(copertura))
            print("Costo: "+str(costo))
            print("Affidabilita: "+str(affidabilita))
            print("Livello: ",livello)

        

#P5
def stampaDatiPolizza():
    polizza = input_polizza()
    print(polizza)
    if polizza not in listaPolizze.values():
        print("Errore, la polizza inserita non è esistente")
    else:
        print(f"Polizza{polizza}: ")
        for robe in listaPolizze.items:
            chiave,tipoPolizza,(copertura,costo,affidabilita),livello =robe

            print("Cliente: "+chiave) 
            print("Copertura: ",str(copertura))
            print("Costo: "+str(costo))
            print("Affidabilita: "+str(affidabilita))
            print("Livello: ",livello)



def input_nominativo():
    nome=input("Inserisci il nome: ")
    while(len(nome)== 0):
        nome=input("Errore, inserisci il nome: ")

    cognome=input("Inserisci il cognome: ")
    while(len(cognome)== 0):
        cognome=input("Errore, inserisci il nome: ")

    nominativo = cognome+" "+nome
    return nominativo


def input_polizza():
    arrayPolizze=["Auto","Casa","Salute","Viaggi"]
    polizza= input("Inserisci il tipo di polizza (Auto,Casa,Salute,Viaggi): ")
    while(polizza not in arrayPolizze):
        if(polizza not in arrayPolizze):
            print("Errore, inserimento sbagliato.")
            polizza= input("Inserisci il tipo di polizza (Auto,Casa,Salute,Viaggi): ")
    return polizza
popola()
aggiungiMe()
aggiungiPolizza()
stampaCliente()
stampaDatiPolizza()

    
