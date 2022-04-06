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
count = 0

for index, line in renamed_df.iterrows():
	if line['tese-dissertacao'] == None:
		count+=1
# print(count)

# print(temp['tese-dissertacao'].to_string())

# dissertacoes_df = renamed_df[is_dissertacao]
# no_category = renamed_df[nor_tese_nor_dis]

# no category: 124, 140, 1444, 1882, 2161

teses = renamed_df[is_tese]
dissertacoes = renamed_df[is_dissertacao]

print(teses)
print(dissertacoes)

teses.to_csv("filtro_teses.csv", index=False)
dissertacoes.to_csv("filtro_dissercoes.csv", index=False)
