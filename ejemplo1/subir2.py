import csv
from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

csv_file = '/home/jeanproject/Documentos/Semana6/clase06-1bim-JeanDavidVasquez/ejemplo1/data/saludos_mundo.csv'

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

with open(csv_file, newline='', encoding='latin-1') as f:
    #convierto cada fila del CSV en un diccionario, donde las claves son los nombres de las columnas.
    reader = csv.DictReader(f)
    #creo una lista con solo las filas que no estén completamente vacías.
    documentos = [row for row in reader if any(row.values())]  # Ignorar filas vacías


miSaludo = Saludo()
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
