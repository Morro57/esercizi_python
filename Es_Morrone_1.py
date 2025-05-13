class Macchina:
    def __init__(self, targa, marca, modello, anno):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def __str__(self):
        return f"targa = {self.targa}, marca = {self.marca}, modello = {self.modello}, anno = {self.anno}"


class Garage:
    def __init__(self):
        self.macchine = []

    def aggiungi_macchina(self, macchina):
            self.macchine.append(macchina)
            print("Macchina aggiunta al garage!")

    def rimuovi_macchina(self, targa):
        for macchina in self.macchine:
            if(macchina.targa == targa):
                self.macchine.remove(macchina)
                return "Macchina rimossa dal garage!"
        print("Macchina non presente nel garage")

    def elenco_macchine(self):
        cont = 0
        for macchina in self.macchine:
            print(macchina)
            cont += 1
        if(cont == 0):
            print("Non sono presenti macchine nel garage.")

    def cerca_macchina(self, targa):
        for macchina in self.macchine:
            if(macchina.targa == targa):
                print(macchina)
                return "Macchina rimossa dal garage!"
        print("Macchina non presente nel garage")

garage = Garage()
while True:
    scelta=int(input("Menù:\n1.Aggiungi una macchina al garage;\n2.Rimuovi una macchina dal garage;\n3.Visualizza elenco macchine presenti;\n4.Cerca la macchina;\n5.Esci.\n"))
    if(scelta> 5 or scelta<1):
        print("Errore, digitazione inserita errata.")
    elif(scelta == 1):
        while True:
            anno = int(input("Inserire l'anno di immatricolazione: "))
            if(anno<1):
                print("Errore, digitazione inserita errata.")
            else:
                break

        while True:
            marca = input("Inserire la marca della macchina: ")
            if(len(marca)<1):
                print("Errore,mancata digitazione.")
            else:
                break
        
        while True:
            modello = input("Inserire il modello della macchina: ")
            if(len(modello)<1):
                print("Errore,mancata digitazione.")
            else:
                break

        while True:
            targa = input("Inserire la targa della macchina: ")
            if(len(targa)==6):
                print("Errore,mancata digitazione o sbagliata.")
            else:
                break
        #print(targa,marca,modello,anno)
        macchina = Macchina(targa,marca,modello,anno)
        #print(macchina)
        garage.aggiungi_macchina(macchina)
    
    elif(scelta == 2):
        while True:
            targa = input("Inserire la targa della macchina: ")
            if(len(targa)==6):
                print("Errore,mancata digitazione o sbagliata.")
            else:
                break
        garage.rimuovi_macchina(targa)

    elif(scelta == 3):
        garage.elenco_macchine()
    elif(scelta == 4):
        while True:
            targa = input("Inserire la targa della macchina: ")
            if(len(targa)==6):
                print("Errore,mancata digitazione o sbagliata.")
            else:
                break
        garage.cerca_macchina(targa)
    elif(scelta == 5):
        print("Programma terminato!")
        break