from os import rename
from pandas_ods_reader import read_ods;
import pandas as pd;

base_path = "referencias_arquivisticas.ods"
sheet_index = 1
df = read_ods(base_path, sheet_index)


change_labels = {
	"TESE / DISSERTAÇÃO": "tese-dissertacao",
	"INSTITUIÇÃO": "instituicao",
	"PROGRAMA": "programa",
	"AUTOR DA T/D": "autor-da-tese-ou-dissertacao",
	"AUTOR 1 DA REF": "autor-1-da-ref",
	"AUTOR 2 DA REF": "autor-2-da-ref",
	"AUTOR 3 DA REF": "autor-3-da-ref",
	"PAÍS": "pais",
	"IDIOMA 1": "idioma-1",
	"ANO 1": "ano-1",
	"TÍTULO DA REFERÊNCIA": "titulo-da-referencia",
	"CLASSIFICAÇÃO BIBLIOGRÁFICA": "classificacao-bibliografica",
	"CITAÇÃO": "citacao",
	"REVISTA/LIVRO/EVENTO": "revista-livro-evento",
}

renamed_df = df.rename(columns=change_labels, inplace=False)

# print(len(renamed_df))
is_tese = renamed_df['tese-dissertacao'] == 'T'
is_dissertacao = renamed_df['tese-dissertacao'] == 'D'
nor_tese_nor_dis = renamed_df['tese-dissertacao'] == None

teses_df = renamed_df[is_tese]
temp = renamed_df.iloc[[122]]
print(temp['tese-dissertacao'])
dissertacoes_df = renamed_df[is_dissertacao]
no_category = renamed_df[nor_tese_nor_dis]

print(len(teses_df))
print(len(dissertacoes_df))
print(len(no_category))
print(len(teses_df) + len(dissertacoes_df))

# no category: 124, 140, 1444, 1882, 2161

df.to_csv("referencias_arquivisticas.csv", index=False)
