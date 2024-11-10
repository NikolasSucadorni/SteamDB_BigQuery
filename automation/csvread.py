import pandas as pd
from pandas_gbq import to_gbq
from google.cloud import bigquery
from google.oauth2 import service_account

df = pd.read_csv("data_steam_sales.csv", sep=",")
df = df.iloc[:, :-2]

df['Game'] = df['Game'].str.replace(r'Play For Freeall-time low:R\$ \d+,\d{2}|Play For Freenew historical|-30%|-33%|Midweek Deal|Top Seller|Daily Deal|™Top Seller|new historical low|Week Long DealTop Seller', '', regex=True)
df['Game'] = df['Game'].str.replace(r'\bat\b$', '', regex=True)
df['Game'] = df['Game'].str.strip()

# Configuração das credenciais
credentials = service_account.Credentials.from_service_account_file("C:/Users/nikol/OneDrive/Documentos/case-steamdb-0d9bb82a98ba.json")

# Definir o nome completo da tabela no BigQuery no formato project.dataset.table
table_id = "case-steamdb.steamDBcase001.steam_DBcase"

# Carregar o DataFrame no BigQuery
to_gbq(df, table_id, project_id="case-steamdb", if_exists="replace", credentials=credentials)