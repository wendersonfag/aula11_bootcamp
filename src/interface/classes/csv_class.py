import pandas as pd



class CsvProcesso:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    ## receber um str str[] recebe uma lista e 
    def filtrar_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        self.df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return self.df_filtrado
        else:
            # fazer recursividade
            return self.filtrar_por(colunas[1:], atributos[1:])
        
    
    # def sub_filtro(self, coluna, atributo):
    #     return self.df_filtrado[self.df_filtrado[coluna] == atributo]


