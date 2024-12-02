from database_setup import create_database
from populate_database import populate_database

def main():
    print("Creando base de datos...")
    create_database()
    
    print("Cargando datos en la base de datos...")
    populate_database()

    print("Flujo completado exitosamente.")

if __name__ == "__main__":
    main()