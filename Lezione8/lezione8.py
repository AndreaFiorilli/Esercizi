class Contatore:
    def __init__(self,conteggio:int=0):
        self.conteggio=0
    
    def setZero(self):
        self.conteggio=0
        
    def add1(self):
        self.conteggio += 1
        
    def sub1(self):
        if self.conteggio == 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self.conteggio -= 1
            
    def get(self):
        return self.conteggio
        
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")



class RecipeManager:
    def __init__(self,recipe:dict={}):
        self.recipe={}
    
    def create_recipe(self,name,ingredient):
        if not name in self.recipe:
            self.recipe[name]=ingredient
        else:
            print("error")
        return self.recipe
            
    def add_ingredient(self,recipe_name,ingredient):
        if not recipe_name in self.recipe:
            self.recipe[recipe_name]=ingredient
        else:
            self.recipe[recipe_name].append(ingredient)
        return self.recipe
            
    def remove_ingredient(self,recipe_name,ingredient):
        if recipe_name in self.recipe:
            if ingredient in self.recipe[recipe_name]:
                self.recipe[recipe_name].remove(ingredient)
        return self.recipe
                
    def update_ingredient(self,recipe_name,old_ingredient,new_ingredient):
        if recipe_name in self.recipe:
            if old_ingredient in self.recipe[recipe_name]:
                idx = self.recipe[recipe_name].index(old_ingredient)
                self.recipe[recipe_name][idx]=new_ingredient
        return self.recipe
                
    def list_recipes(self):
        lista=[]
        for i in self.recipe:
            lista.append(i)
        return lista
        
    def list_ingredients(self,recipe_name): 
        for i in self.recipe:
            if i == recipe_name:
                return self.recipe[recipe_name]
                
    def search_recipe_by_ingredient(self,ingredient):
        for name in self.recipe:
            for a in self.recipe[name]:
                if ingredient in a:
                    return self.recipe




class Veicolo:
    def __init__(self,marca:str,modello:str,anno:int):
        self.marca=marca
        self.modello=modello
        self.anno=anno
    
    def descrivi_veicolo(self):
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
        
class Auto(Veicolo):
    def __init__(self,marca:str,modello:str,anno:int,numero_porte:int):
        Veicolo.__init__(self,marca,modello,anno)
        self.numero_porte=numero_porte
    
    def descrivi_veicolo(self):
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        
class Moto(Veicolo):
    def __init__(self,marca:str,modello:str,anno:int,tipo:str):
        Veicolo.__init__(self,marca,modello,anno)
        self.tipo=tipo
    
    def descrivi_veicolo(self):
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")