from enum import auto
from tkinter.tix import Tree
from pandas_ods_reader import read_ods;
import pandas as pd;

from config import SPREADSHEET, SRC_DIR, OUTPUT_DIR

def remove_undesired_column(df, column_name):
	df = df.drop(column_name, axis=1)
	return df

def create_new_column(df, column_name, values):
	if len(df) != len(values):
		print("Não é possível criar nova coluna (linhas sem correspondente)!")
		return
	df.insert(4, column_name, values, True)
	return df

def reduce_autor_ref(df):
	merged_values = []
	for i in df.index:
		autores = ''
		for j in range(3):
			if df['autor-'+str(j+1)+'-da-ref'][i] != None:
				autores += df['autor-'+str(j+1)+'-da-ref'][i] + "||"
		merged_values.append(autores[:len(autores)-2])
	
	df = create_new_column(df, "autores-da-ref", merged_values)
	for i in range(3): df = remove_undesired_column(df, 'autor-'+str(i+1)+'-da-ref')
	return df

base_path = SRC_DIR + '/' + SPREADSHEET
sheet_index = 1
df = read_ods(base_path, sheet_index)

# renomeio temporario
change_labels = {
	"TESE / DISSERTAÇÃO": "tese-dissertacao",
	"INSTITUIÇÃO": "instituicao",
	"PROGRAMA": "programa",
	"AUTOR DA T/D": "autor-da-tese-ou-dissertacao",
	"AUTOR 1 DA REF": "autor-1-da-ref",
	"AUTOR 2 DA REF": "autor-2-da-ref",
	"AUTOR 3 DA REF": "autor-3-da-ref",
	"PAÍS": "pais",
	"IDIOMA 1": "idioma",
	"ANO 1": "ano",
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

if count > 0:
	print("Verifique a classificação da referência! (tese / dissertação)")
else:
	# print(temp['tese-dissertacao'].to_string())

	# dissertacoes_df = renamed_df[is_dissertacao]
	# no_category = renamed_df[nor_tese_nor_dis]

	# no category: 124, 140, 1444, 1882, 2161

	teses = renamed_df[is_tese]
	teses = remove_undesired_column(teses, "unnamed.1")
	teses = remove_undesired_column(teses, "tese-dissertacao")
	teses = reduce_autor_ref(teses)
	
	dissertacoes = renamed_df[is_dissertacao]
	dissertacoes = remove_undesired_column(dissertacoes, "unnamed.1")
	dissertacoes = remove_undesired_column(dissertacoes, "tese-dissertacao")
	dissertacoes = reduce_autor_ref(dissertacoes)

	# print(teses)
	# print(dissertacoes)

	teses.to_csv(OUTPUT_DIR + '/filtro_teses.csv', index=False)
	dissertacoes.to_csv(OUTPUT_DIR + '/filtro_dissertacoes.csv', index=False)
