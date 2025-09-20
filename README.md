# Comparativas De Construcción Genshin

Este proyecto permite guardar, consultar, comparar y exportar builds de personajes de Genshin Impact. Las builds se almacenan en formato JSON y se pueden exportar a CSV (con filtros), lo que facilita la actualización y análisis de tu base de datos personal.

## Funcionalidades

- Añadir builds de personajes con toda la información relevante.
- Listar todas las builds guardadas.
- Buscar builds por personaje, artefacto o estadística.
- Eliminar builds.
- Exportar builds a CSV (puedes filtrar por personaje, artefacto o estadística antes de exportar).

## Uso

1. Ejecuta el script principal:

   ```bash
   python comparativas_genshin.py
   ```

2. Sigue el menú interactivo para agregar, consultar, buscar, eliminar y exportar builds.

## Exportación filtrada a CSV

Al elegir la opción de exportar, puedes:
- Exportar todas las builds.
- Filtrar por personaje.
- Filtrar por artefacto (familia y tipo).
- Filtrar por estadística.

El archivo CSV generado se llama `comparativas.csv` y contiene los siguientes campos:

- personaje
- familia_artefacto
- tipo_artefacto
- arma
- nivel
- talentos
- estadisticas
- notas

## Requisitos

- Python 3.x
- No requiere librerías externas (usa solo módulos estándar).

## Estructura de archivos

- `comparativas_genshin.py`: Script principal con todas las funcionalidades.
- `comparativas.json`: Base de datos local con las builds guardadas.
- `comparativas.csv`: Archivo generado al exportar builds.

## Ejemplo de uso

```text
--- Comparativas Genshin ---
1. Añadir build
2. Mostrar builds
3. Buscar builds por personaje
4. Buscar builds por artefacto
5. Buscar builds por estadística
6. Eliminar build
7. Exportar builds a CSV
8. Salir
```

## Licencia

GPL
