import pandas as pd

from config import DATA_DIR

file = pd.read_excel(DATA_DIR + 'referencias_arquivisticas.ods')
print(file.head())
#johnatan