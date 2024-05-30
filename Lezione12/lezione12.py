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
                self.catalog[director_name].append(movies)

    def remove_movie(self,director_name,movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)

    def list_directors(self):
        for i in self.catalog:
            print(i)

    def get_movies_by_director(self,director_name): 
        for i in self.catalog:
            if i == director_name:
                return self.catalog[director_name]
            
    def search_movies_by_title(self,title):
        result = {}
        for director, movies in self.catalog.items():
            matching_movies = [movie for movie in movies if title.lower()]
            if matching_movies:
                result[director] = matching_movies

        if result:
            return result
        else:
            return f"Nessun film trovato con la parola '{title}' nel titolo."

moviecatlog=MovieCatalog()
moviecatlog.add_movie("Regista3",["Gran Film"])
moviecatlog.add_movie("Regista2",["Bel Film"])
moviecatlog.add_movie("Regista3",["Grande Film"])
moviecatlog.add_movie("Regista3",["Ottimo Film"])
moviecatlog.add_movie("Regista2",["Fantastico Film"])
print(moviecatlog.catalog)
moviecatlog.remove_movie("Regista3",["Grande Film"])
print(moviecatlog.catalog)
moviecatlog.list_directors()
print(moviecatlog.get_movies_by_director("Regista3"))
moviecatlog.search_movies_by_title("Bel")
