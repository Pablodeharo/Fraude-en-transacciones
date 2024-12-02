import pandas as pd
from sqlalchemy import create_engine

# Configura la conexión a la base de datos SQLite
DATABASE_URI = "sqlite:///fraud_detection.db"

def export_to_csv():
    # Crear una conexión a la base de datos
    engine = create_engine(DATABASE_URI)

    # Leer las tablas desde la base de datos
    df_accounts = pd.read_sql("SELECT * FROM accounts", engine)
    df_transactions = pd.read_sql("SELECT * FROM transactions", engine)

    # Exportar a archivos CSV
    df_accounts.to_csv('accounts.csv', index=False)
    df_transactions.to_csv('transactions.csv', index=False)

    print("Datos exportados a CSV exitosamente.")

if __name__ == "__main__":
    export_to_csv()