import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

with open('data/saludos_mundo.csv', encoding='latin-1') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)
    for row in reader:
        session.add(Saludo2(mensaje=row[0].strip(), tipo=row[1].strip(), origen=row[2].strip()))
session.commit()
