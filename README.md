# Proyecto de Citas Médicas

Scripts para generar datos ficticios de citas médicas, analizarlos y visualizarlos.

## Archivos

- **generar_citas.py** — Genera un CSV con 5000 registros de citas médicas usando Faker.
- **analisis_citas.py** — Análisis descriptivo y predicción lineal de citas por mes.
- **app.py** — Dashboard interactivo con Streamlit y Plotly.
- **requirements.txt** — Lista de dependencias del proyecto.

## Cómo usar

```bash
pip install -r requirements.txt
python generar_citas.py
python analisis_citas.py
streamlit run app.py
```

Ejecutar en orden: primero generar los datos, luego analizar y finalmente el dashboard.
