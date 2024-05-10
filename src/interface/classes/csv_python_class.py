import csv


class CsvProcessarPython:
    def __init__(self, caminho: str):
        self.path = caminho
        self.lista = []
        self.lista_filtrada = []


    def carregar_csv(self):
        """
        Funcao que le um arquivo csv e retorna uma lista
        de dicionarios
        """
        with open(self.path, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                self.lista.append(linha)
        return self.lista
    
    
    def filtra_por(self, coluna: str, atributo: str):
        """
        Funcao que filtra produtos onde entrega = true
        """
        for fitrar in self.lista:
            if fitrar[coluna]== atributo:
                self.lista_filtrada.append(fitrar)
        return self.lista_filtrada


arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessarPython(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtra_por(filtro,limite))