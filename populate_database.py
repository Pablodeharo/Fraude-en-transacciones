import pandas as pd
from sqlalchemy import create_engine
from models import Transaction, Account
from database_setup import DATABASE_URI

def populate_database():
    # Leer el dataset
    df = pd.read_csv(r"C:\Users\Lucas\Desktop\Fraude en transacciones\Data\transacciones.csv")
    
    # Dividir el DataFrame
    df_accounts = df[['AccountID', 'CustomerAge', 'CustomerOccupation', 'AccountBalance']].drop_duplicates()
    df_transactions = df[['TransactionID', 'AccountID', 'TransactionAmount', 'TransactionDate',
                           'TransactionType', 'Location', 'DeviceID', 'IP Address', 'MerchantID',
                           'Channel', 'Anomaly']].copy()  # Copia explícita para evitar warnings
    df_transactions.rename(columns={"IP Address": "IPAddress"}, inplace=True)  # Renombrar columna

    # Validar duplicados
    df_accounts = df_accounts.drop_duplicates(subset=["AccountID"])
    df_transactions = df_transactions.drop_duplicates(subset=["TransactionID"])

    # Conectar a la base de datos
    engine = create_engine(DATABASE_URI)

    # Volcar datos en la base de datos
    try:
        df_accounts.to_sql('accounts', engine, if_exists='append', index=False)
        df_transactions.to_sql('transactions', engine, if_exists='append', index=False)
        print("Datos cargados exitosamente.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")