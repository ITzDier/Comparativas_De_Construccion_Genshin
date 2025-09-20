# Aquí va el contenido de comparativas_genshin.py

# Funcionalidad de exportación filtrada a CSV

def exportar_a_csv(data, filename):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Ejemplo de uso
if __name__ == '__main__':
    datos = [{'Nombre': 'Ejemplo', 'Valor': 1}]
    exportar_a_csv(datos, 'exportado.csv')