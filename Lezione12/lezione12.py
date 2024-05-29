# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python.
# Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi.
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli,
# restituirli e visualizzare quali libri sono disponibili in un dato momento.

class Libro:
    def __init__(self,titolo:str,autore:str,stato:bool=True)->None:
        self.titolo=titolo
        self.autore=autore
        self.stato=stato

class Biblioteca:
    def __init__(self,libri:list=[])->None:
        self.libri=[]

    def aggiungi_libro(self,libro:Libro):
        self.libri.append(libro)
    
    def presta_libro(self,titolo:str):
        for i in self.libri:
            if titolo == i.titolo and i.stato==True:
                print("Libro prestato") 
                break
            else:
                print("Libro non disponibile o già prestato")
                break

    def restituisci_libro(self,titolo:str):
        for i in self.libri:
            if titolo == i.titolo and i.stato==False:
                print("Libro disponibile")
                i.stato=True
    
    def mostra_libri_disponibili(self,):
        libri_disp=[]
        for i in self.libri:
            if i.stato==True:
                libri_disp.append(i.titolo)
        if not libri_disp:
            print("Non ci sono libri disponibili")
        else:
            print(libri_disp)

libro1=Libro("Titolo1","Autore")
libro2=Libro("Titolo2","Autore",False)
libro3=Libro("Titolo3","Autore")
biblioteca=Biblioteca()
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)
biblioteca.presta_libro("Titolo1")
#biblioteca.restituisci_libro("Titolo2")
biblioteca.mostra_libri_disponibili()


# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere,
# rimuovere e cercare film di un particolare regista.
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

class MovieCatalog:
    def __init__(self,catalog:dict={})->None:
        self.catalog={}
    
    def add_movie(self,director_name,movies):
            if not director_name in self.catalog:
                self.catalog[director_name]=movies
            else:
                movies.append(movies)
                self.catalog[director_name]=movies
            print(self.catalog)




moviecatlog=MovieCatalog()
moviecatlog.add_movie("Regista3",["Gran Film"])
moviecatlog.add_movie("Regista2",["Bel Film"])
moviecatlog.add_movie("Regista3",["Grande Film"])