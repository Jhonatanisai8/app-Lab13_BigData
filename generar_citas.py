import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('es_ES')

n = 5000

especialidades = [
    'Medicina General',
    'Pediatría',
    'Cardiología',
    'Traumatología',
    'Ginecología',
    'Dermatología'
]

estados = [
    'Atendida',
    'Cancelada',
    'No asistió'
]

datos = []

for i in range(n):
    datos.append([
        i+1,
        fake.date_between('-1y','today'),
        np.random.choice(especialidades),
        np.random.choice(estados,p=[0.75,0.15,0.10]),
        np.random.randint(15,90)
    ])

df = pd.DataFrame(datos,
                  columns=[
                      'id_cita',
                      'fecha',
                      'especialidad',
                      'estado',
                      'edad'
                  ])

print(df.head())
df.to_csv('citas_medicas.csv',index=False)
print("\nArchivo 'citas_medicas.csv' generado con éxito.")
