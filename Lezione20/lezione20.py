class Pagamento:
    def __init__(self):
        self.__importo=0.0

    def getImporto(self):
        return self.__importo
    
    def setImporto(self,importo:float):
        self.__importo=importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento: ${self.getImporto():.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self,importo):
        super().__init__()
        self.setImporto(importo)

    def dettagliPagamento(self):
        print(f"Importo del pagamento: $ {self.getImporto()} in contanti")

    def inPezziDa(self):
        importo=self.getImporto()
        float(importo)
        moneta05=0
        moneta010=0
        moneta020=0
        moneta050=0
        moneta1=0
        moneta2=0
        banconota5=0  
        banconota10=0
        banconota20=0
        banconota50=0
        banconota100=0
        banconota200=0
        banconota500=0
        while importo!=0:
            if importo >=500:
                importo=importo-500
                banconota500 += 1
            elif importo >=200:
                importo=importo-200
                banconota200 += 1
            elif importo >100:
                importo=importo-100
                banconota100 += 1
            elif importo >=50:
                importo=importo-50
                banconota50 += 1
            elif importo >=20:
                importo=importo-20
                banconota20 += 1
            elif importo >=10:
                importo=importo-10
                banconota10 += 1
            elif importo >=5:
                importo=importo-5
                banconota5 += 1
            elif importo >= 2:
                importo=importo-2
                moneta2 += 1
            elif importo >= 1:
                importo=importo-1
                moneta1 += 1
            elif importo >= 0.50:
                importo=importo-0.50
                moneta050 += 1
            elif importo >= 0.20:
                importo=importo-0.20
                moneta020 = moneta020+ 1
            elif importo >= 0.10:
                importo=importo-0.10
                moneta010 += 1
            elif importo >= 0.05:
                importo=importo-0.05
                moneta05 += 1
 
        if banconota500>0:
                print(f"{banconota500} da 500 euro")
        if banconota200 >0:
                print(f"{banconota200} da 200 euro")
        if banconota100 >0:
                print(f"{banconota100} da 100 euro")
        if banconota50 >0:
                print(f"{banconota50} da 50 euro")
        if banconota20 >0:
                print(f"{banconota20} da 20 euro")
        if banconota10 >0:
                print(f"{banconota10} da 10 euro")
        if banconota5 >0:
                print(f"{banconota5} da 5 euro")
        if moneta2 >0:
                print(f"{moneta2} da 2 euro")
        if moneta1 >0:
                print(f"{moneta1} da 1 euro")
        if moneta050 >0:
                print(f"{moneta050} da 0.050 euro")
        if moneta020 >0:
                print(f"{moneta020} da 0.20 euro")
        if moneta010 >0:
                print(f"{moneta010} da 0.10 euro")
        if moneta05 >0:
                print(f"{moneta05} da 0.05 euro")
        
        
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self,importo,titolare,datascadenza,numerocarta):
        super().__init__()
        self.setImporto(importo)
        self.titolare=titolare
        self.datascadenza=datascadenza
        self.numerocarta=numerocarta
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: $ {self.getImporto()} con la carta")
        print(f"Nome sulla carta: {self.titolare}\nData di scadenza: {self.datascadenza}\nNumero della carta: {self.numerocarta}")
        
        
        


pc=PagamentoContanti(150)
pc.dettagliPagamento()
pc.inPezziDa()
pcdc=PagamentoCartaDiCredito(150,"Andrea","11/27",2389472394820)
pcdc.dettagliPagamento()