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

df_teses = pd.DataFrame(columns=list(change_labels.values()))
df_dissertacoes = pd.DataFrame(columns=list(change_labels.values()))

print(len(renamed_df))

# df.to_csv("referencias_arquivisticas.csv", index=False)
