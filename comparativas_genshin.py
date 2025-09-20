import json
import os
import csv

DATA_FILE = "comparativas.json"
CSV_FILE = "comparativas.csv"

def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

def agregar_build():
    print("=== Añadir nueva build de personaje ===")
    personaje = input("Nombre del personaje: ")
    familia_artefacto = input("Familia de artefacto (ej. Emblema del Destino): ")
    tipo_artefacto = input("Tipo de artefacto (ej. 4 piezas, 2+2 piezas): ")
    arma = input("Arma utilizada: ")
    nivel = input("Nivel del personaje: ")
    talentos = input("Talentos (ej. 10/10/10): ")
    estadisticas = input("Estadísticas globales (ej. ATK, CRIT, etc.): ")
    notas = input("Notas adicionales: ")

    build = {
        "personaje": personaje,
        "familia_artefacto": familia_artefacto,
        "tipo_artefacto": tipo_artefacto,
        "arma": arma,
        "nivel": nivel,
        "talentos": talentos,
        "estadisticas": estadisticas,
        "notas": notas
    }

    datos = cargar_datos()
    datos.append(build)
    guardar_datos(datos)
    print("Build guardada correctamente.")

def mostrar_builds():
    datos = cargar_datos()
    if not datos:
        print("No hay builds guardadas.")
        return
    print("=== Builds guardadas ===")
    for idx, build in enumerate(datos, 1):
        print(f"\n[{idx}] Personaje: {build['personaje']}")
        print(f"  Familia artefacto: {build['familia_artefacto']}")
        print(f"  Tipo artefacto: {build['tipo_artefacto']}")
        print(f"  Arma: {build['arma']}")
        print(f"  Nivel: {build['nivel']}")
        print(f"  Talentos: {build['talentos']}")
        print(f"  Estadísticas: {build['estadisticas']}")
        print(f"  Notas: {build['notas']}")

def buscar_por_personaje():
    datos = cargar_datos()
    if not datos:
        print("No hay builds guardadas.")
        return
    nombre = input("Escribe el nombre del personaje a buscar: ").strip().lower()
    resultados = [b for b in datos if nombre in b['personaje'].strip().lower()]
    if not resultados:
        print("No se encontraron builds para ese personaje.")
    else:
        print(f"=== Builds para '{nombre.title()}' ===")
        for idx, build in enumerate(resultados, 1):
            print(f"\n[{idx}] Familia artefacto: {build['familia_artefacto']}")
            print(f"  Tipo artefacto: {build['tipo_artefacto']}")
            print(f"  Arma: {build['arma']}")
            print(f"  Nivel: {build['nivel']}")
            print(f"  Talentos: {build['talentos']}")
            print(f"  Estadísticas: {build['estadisticas']}")
            print(f"  Notas: {build['notas']}")

def buscar_por_artefacto():
    datos = cargar_datos()
    if not datos:
        print("No hay builds guardadas.")
        return
    familia = input("Escribe la familia de artefacto a buscar: ").strip().lower()
    tipo = input("Escribe el tipo de artefacto a buscar (deja vacío para ignorar): ").strip().lower()
    resultados = []
    for b in datos:
        cond_fam = familia in b['familia_artefacto'].strip().lower()
        cond_tipo = tipo in b['tipo_artefacto'].strip().lower() if tipo else True
        if cond_fam and cond_tipo:
            resultados.append(b)
    if not resultados:
        print("No se encontraron builds con esos artefactos.")
    else:
        print(f"=== Builds con familia '{familia.title()}' y tipo '{tipo.title() if tipo else 'Cualquiera'}' ===")
        for idx, build in enumerate(resultados, 1):
            print(f"\n[{idx}] Personaje: {build['personaje']}")
            print(f"  Familia artefacto: {build['familia_artefacto']}")
            print(f"  Tipo artefacto: {build['tipo_artefacto']}")
            print(f"  Arma: {build['arma']}")
            print(f"  Nivel: {build['nivel']}")
            print(f"  Talentos: {build['talentos']}")
            print(f"  Estadísticas: {build['estadisticas']}")
            print(f"  Notas: {build['notas']}")

def buscar_por_estadistica():
    datos = cargar_datos()
    if not datos:
        print("No hay builds guardadas.")
        return
    estadistica = input("Escribe la estadística a buscar (ej. CRIT, ATK): ").strip().lower()
    resultados = [b for b in datos if estadistica in b['estadisticas'].strip().lower()]
    if not resultados:
        print("No se encontraron builds con esa estadística.")
    else:
        print(f"=== Builds con estadística '{estadistica.upper()}' ===")
        for idx, build in enumerate(resultados, 1):
            print(f"\n[{idx}] Personaje: {build['personaje']}")
            print(f"  Familia artefacto: {build['familia_artefacto']}")
            print(f"  Tipo artefacto: {build['tipo_artefacto']}")
            print(f"  Arma: {build['arma']}")
            print(f"  Nivel: {build['nivel']}")
            print(f"  Talentos: {build['talentos']}")
            print(f"  Estadísticas: {build['estadisticas']}")
            print(f"  Notas: {build['notas']}")

def filtrar_para_exportar(datos):
    print("\n¿Quieres filtrar las builds antes de exportar?")
    print("1. No filtrar (exportar todas)")
    print("2. Filtrar por personaje")
    print("3. Filtrar por artefacto (familia y tipo)")
    print("4. Filtrar por estadística")
    op = input("Selecciona una opción: ")
    if op == "1":
        return datos
    elif op == "2":
        nombre = input("Nombre del personaje (filtro): ").strip().lower()
        return [b for b in datos if nombre in b['personaje'].strip().lower()]
    elif op == "3":
        familia = input("Familia de artefacto (filtro): ").strip().lower()
        tipo = input("Tipo de artefacto (filtro, opcional): ").strip().lower()
        filtrados = []
        for b in datos:
            cond_fam = familia in b['familia_artefacto'].strip().lower()
            cond_tipo = tipo in b['tipo_artefacto'].strip().lower() if tipo else True
            if cond_fam and cond_tipo:
                filtrados.append(b)
        return filtrados
    elif op == "4":
        estadistica = input("Estadística (filtro): ").strip().lower()
        return [b for b in datos if estadistica in b['estadisticas'].strip().lower()]
    else:
        print("Opción no válida, exportando todas las builds.")
        return datos

def exportar_a_csv():
    datos = cargar_datos()
    if not datos:
        print("No hay builds guardadas.")
        return
    builds_a_exportar = filtrar_para_exportar(datos)
    if not builds_a_exportar:
        print("No hay builds que cumplan con el filtro.")
        return
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "personaje", "familia_artefacto", "tipo_artefacto", "arma", "nivel", "talentos", "estadisticas", "notas"
        ])
        writer.writeheader()
        for build in builds_a_exportar:
            writer.writerow(build)
    print(f"Builds exportadas correctamente a '{CSV_FILE}'.")

def eliminar_build():
    datos = cargar_datos()
    mostrar_builds()
    if not datos:
        return
    try:
        idx = int(input("Número de build a eliminar: ")) - 1
        if 0 <= idx < len(datos):
            datos.pop(idx)
            guardar_datos(datos)
            print("Build eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- Comparativas Genshin ---")
        print("1. Añadir build")
        print("2. Mostrar builds")
        print("3. Buscar builds por personaje")
        print("4. Buscar builds por artefacto")
        print("5. Buscar builds por estadística")
        print("6. Eliminar build")
        print("7. Exportar builds a CSV")
        print("8. Salir")
        op = input("Selecciona una opción: ")
        if op == "1":
            agregar_build()
        elif op == "2":
            mostrar_builds()
        elif op == "3":
            buscar_por_personaje()
        elif op == "4":
            buscar_por_artefacto()
        elif op == "5":
            buscar_por_estadistica()
        elif op == "6":
            eliminar_build()
        elif op == "7":
            exportar_a_csv()
        elif op == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()