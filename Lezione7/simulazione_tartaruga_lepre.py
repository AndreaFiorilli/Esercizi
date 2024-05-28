# Andrea Fiorilli
#14/05/24
"""
In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
"""
import random

def Posizioni(posTart:int,posLepre:int)->list:
    lunghezza_lista=70
    percorso:list[int]=["_"]*lunghezza_lista
    percorso[posLepre-1]="H"
    percorso[posTart-1]="T"
    if posLepre==posTart:
        percorso[posLepre-1]="OUCH!!!"
    return percorso
def Tartaruga(i:int)->str:
    mossa=""
    if 1 <= i <= 5:
        mossa="Passo veloce"
        posTart=3
    elif 6 <= i <= 7:
        mossa="Scivolata"
        posTart=6
    elif 8 <= i <= 10:
        mossa="Passo lento"

    return mossa

def Lepre(j:int)->str:
    mossa=""
    if 1 <= j <= 2:
        mossa="Riposo"
    elif 3 <= j <= 4:
        mossa="Grande balzo"
    elif j == 5:
        mossa="Grande scivolata"
    elif 6 <= j <= 8:
        mossa="Piccolo balzo"
    elif 9 <= j <= 10:
        mossa="Piccola scivolata"
    return mossa

posLepre=1
posTart=1
conta=0
energiaTart=100
energiaLepre=100
ostacoli:dict={15:3,30:5,45:7,60:9}
bonus:dict={10:2,20:4,40:6,60:8}    
while posTart != 70 and posLepre != 70:
    i=random.randint(1, 10)
    j=random.randint(1, 10)
    a=random.randint(1, 2)
    tempo=""
    if conta==10:
        if a==1:
            tempo="Soleggiato"
        elif a==2:
            tempo="Piovoso"
        conta=0
    print(f"Tartaruga = {Tartaruga(i)}")
    print(f"Lepre = {Lepre(j)}")
    if Tartaruga(i)== "Passo veloce":
        if energiaTart>5:
            posTart=posTart+3
            energiaTart=energiaTart-5
            for n in ostacoli:
                if posTart == n:
                    posTart -= ostacoli[n]
                    print(f"Tartaruga ostacolo trovato{posTart}")
            for m in bonus:
                if posTart == m:
                    posTart += bonus[m]
                    print(f"Tartaruga bonus trovato{posTart}")
            if energiaTart<=0:
                energiaTart=0
            if posTart>70:
                posTart=70
            print(posTart)
            if tempo=="Piovoso":
                posTart=posTart-1
                print(f"Tempo piovoso,Tartaruga penalità -1: {posTart}")
        else:
            print(f"Energia non sufficiente \n Energia guadagnata: +10")
            energiaTart=energiaTart+10
            if energiaTart>=100:
                energiaTart=100
    elif Tartaruga(i)== "Scivolata":
        if energiaTart>10:
            posTart=posTart-6
            energiaTart=energiaTart-10
            for n in ostacoli:
                if posTart == n:
                    posTart -= ostacoli[n]
                    print(f"Tartaruga ostacolo trovato {posTart}")
            for m in bonus:
                if posTart == m:
                    posTart += bonus[m]
                    print(f"Tartaruga bonus trovato{posTart}")
            if energiaTart<=0:
                energiaTart=0
            if posTart<1:
                posTart=1
            print(posTart)
            if tempo=="Piovoso":
                posTart=posTart-1
                print(f"Tempo piovoso,Tartaruga penalità -1: {posTart}")
        else:
            print(f"Energia non sufficiente \n Energia guadagnata: +10")
            energiaTart=energiaTart+10
            if energiaTart>=100:
                energiaTart=100
    elif Tartaruga(i)== "Passo lento":
        if energiaTart>3:
            posTart=posTart+1
            energiaTart=energiaTart-3
            for n in ostacoli:
                if posTart == n:
                    posTart -= ostacoli[n]
                    print(f"Tartaruga ostacolo trovato{posTart}")
            for m in bonus:
                if posTart == m:
                    posTart += bonus[m]
                    print(f"Tartaruga bonus trovato{posTart}")
            if energiaTart<=0:
                energiaTart=0
            if posTart>70:
                posTart=70
            print(posTart)
            if tempo=="Piovoso":
                posTart=posTart-1
                print(f"Tempo piovoso,Tartaruga penalità -1: {posTart}")
        else:
            print(f"Energia non sufficiente \n Energia guadagnata: +10")
            energiaTart=energiaTart+10
            if energiaTart>=100:
                energiaTart=100


    if Lepre(j)== "Riposo":
        posLepre=posLepre+0
        energiaLepre=energiaLepre+10
        if energiaLepre>=100:
            energiaLepre=100
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")
    elif Lepre(j)== "Grande balzo":
        posLepre=posLepre+9
        energiaLepre=energiaLepre-15
        for n in ostacoli:
            if posLepre == n:
                posLepre -= ostacoli[n]
                print(f"Lepre ostacolo trovato{posLepre}")
        for m in bonus:
            if posLepre == m:
                posLepre += bonus[m]
                print(f"Lepre bonus trovato{posLepre}")
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre>70:
            posLepre=70
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")

    elif Lepre(j)== "Grande scivolata":
        posLepre=posLepre-12
        energiaLepre=energiaLepre-20
        for n in ostacoli:
                if posLepre == n:
                    posLepre -= ostacoli[n]
                    print(f"Lepre ostacolo trovato{posLepre}")
        for m in bonus:
            if posLepre == m:
                posLepre += bonus[m]
                print(f"Lepre bonus trovato{posLepre}")
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre<1:
            posLepre=1
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")

    elif Lepre(j)== "Piccolo balzo":
        posLepre=posLepre+1
        energiaLepre=energiaLepre-5
        for n in ostacoli:
                if posLepre == n:
                    posLepre -= ostacoli[n]
                    print(f"Lepre ostacolo trovato{posLepre}")
        for m in bonus:
            if posLepre == m:
                posLepre += bonus[m]
                print(f"Lepre bonus trovato{posLepre}")
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre>70:
            posLepre=70
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")

    elif Lepre(j)== "Piccola scivolata":
        posLepre=posLepre-2
        energiaLepre=energiaLepre-8
        for n in ostacoli:
                if posLepre == n:
                    posLepre -= ostacoli[n]
                    print(f"Lepre ostacolo trovato{posLepre}")
        for m in bonus:
            if posLepre == m:
                posLepre += bonus[m]
                print(f"Lepre bonus trovato{posLepre}")
        if energiaLepre<=0:
            energiaLepre=0
        if posLepre<1:
            posLepre=1
        print(posLepre)
        if tempo=="Piovoso":
            posLepre=posLepre-2
            print(f"Tempo piovoso,Lepre penalità -2: {posLepre}")
    print(Posizioni(posTart,posLepre))
    conta=conta+1
if posLepre >= 70:
    print("HARE WINS || YUCH!!!")
elif posTart >= 70:
    print("TORTOISE WINS! || VAY!!!")
elif posTart==posLepre:
    print("IT'S A TIE")
