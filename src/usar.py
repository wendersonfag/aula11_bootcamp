from interface.classes.csv_class import CsvProcesso

arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'



arquivo_CSV = CsvProcesso(arquivo_csv)
arquivo_CSV.carregar_csv() # Load the csv
print(arquivo_CSV.filtrar_por(['estado','preço'], ['SP','10,50'])) # filtra DF


# print(arquivo_CSV.filtrar_por('preço', '10,50'))
# print(arquivo_CSV.carregar_csv())

# arquivo_csv = './exemplo2.csv'
# filtro = 'estado'
# limite = 'DF'



# arquivo_CSV = CsvProcesso(arquivo_csv)
# arquivo_CSV.carregar_csv()
# print(arquivo_CSV.filtrar_por(filtro, limite))