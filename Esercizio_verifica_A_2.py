
citta=(("Monza", [("Gennaio", 85),("Febbraio",75 ),("Marzo",65)]),
       ("Brescia",[("Gennaio",45),("Febbraio",55),("Marzo",35)]),
       ("Como",[("Gennaio",70),("Febbraio",60),("Marzo",50)])
       )


  
def stampaTupla(citta):

    trovato=False
    while True:
        cittaInput=input("Inserisci il capoluogo da visualizzare i suoi dati pluviometrici: ")
        for capoluogo,rilevazione in citta:
            if(cittaInput==capoluogo):
                trovato=True

        if not trovato:
                print("Città non trovata.")
        else:
            break
    media=0
    cont=0
    valoreMax=0
    meseMax=[]
    valoreMin=1000
    meseMin=[]

    for capoluogo,rilevazioni in citta:
        #print(rilevazioni,type(rilevazioni))
        for mese,dato in rilevazioni:
            cont+=1
            media+=dato
            if(valoreMax<dato):
                valoreMax=dato
                meseMax=[mese]
            elif(valoreMax==dato):
                meseMax=[mese]

            if(valoreMin>dato):
                valoreMin=dato
                meseMin=[mese]
            elif(valoreMin==dato):
                meseMin=[mese]
    media/=cont

    tupla=(media,(valoreMax,meseMax),(valoreMin,meseMin))

    return tupla

print(stampaTupla(citta))