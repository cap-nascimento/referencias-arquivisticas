import pandas as pd
import requests

from config import LINKS, SRC_DIR, OUTPUT_DIR

requests.packages.urllib3.disable_warnings()

# Abre o arquivo de links usando a biblioteca pandas
dfs = pd.read_excel(SRC_DIR + '/' + LINKS, sheet_name=None)

resultado = open(OUTPUT_DIR + '/' + 'resultado.csv', "a+")

# Cria o cabeçalho do arquivo csv de resultado
resultado.write("TESE / DISSERTAÇÃO;TITULO DA REFERÊNCIA;LINK;STATUS LINK\n")

count = 0

# Loop nas tabelas do arquivo de links
for name, sheet in dfs.items():

    # Loop nas linhas das tabelas do arquivo de links
    for index, linha in sheet.iterrows():
        
        print(count, end="\r")

        # Verificação do link
        status = "OK"
        try:
            r = requests.get(linha["LINK"], verify=False)

            # O Status 200 significa que a pagina foi retornada sem erros
            if r.status_code != 200:
                status = "Erro"
        except Exception as e:
            print(e)
            status = "Erro"

        # Guardando a linha no arquivo csv de resultado
        resultado.write("{};{};{};{}\n".format(linha["TESE / DISSERTAÇÃO"], linha["TÍTULO DA REFERÊNCIA"], linha["LINK"], status))
        count = count + 1
