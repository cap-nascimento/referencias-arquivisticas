# -*- coding: utf-8 -*-
import pandas as pd
import requests
import math
import re
from os.path import exists
import os

requests.packages.urllib3.disable_warnings()

def formatar(campo):
    #if isinstance(campo, float):
    #    if math.isnan(campo):
    #        campo = ""
    if campo == "nan":
        campo = ""
    if isinstance(campo, str):
        campo = campo.replace(";", ",").replace(":", ": ").replace("\n", "")
    return campo


def testar_link(link):
    status = "NONE"
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        r = requests.get(link, headers=headers, verify=False, timeout=5)
        if r.status_code == 200 or r.status_code == None:
            status = "Ok"
        else:
            status = "Erro"
    except Exception as e:
        status = "Erro"
    return status


def gerar_csv(nome, sheet):
    nome_arquivo = nome + "_resultado.csv"
    if exists(nome_arquivo):
        os.remove(nome_arquivo)
    resultado = open(nome_arquivo, "w+", errors="ignore")
    cols = len(sheet.columns)
    resultado.write("{};STATUS LINK\n".format(";".join(sheet.columns)))
    for index, linha in sheet.iterrows():
        print("{} => {}".format(nome, str(index)))
        registro = ""
        for col in range(0, cols):
            valor = str(linha[col])
            registro = registro + formatar(valor) + ";"
            if(re.search("http[s]?:\/\/", valor)):
                status = testar_link(valor)
            else:
                status = 'Erro'
        resultado.write(registro + status + '\n')

dfs = pd.read_excel("source/BASE_LINKS_STATUS.xlsx", sheet_name=None)

for nome, sheet in dfs.items():
    gerar_csv(nome, sheet)

# def generate_links():
#     dfs = pd.read_excel("aqui.xlsx", sheet_name=None)

#     for nome, sheet in dfs.items():
#         gerar_csv(nome, sheet)
