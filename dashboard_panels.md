# Paneles de Grafana para el Análisis de Ciberseguridad

A continuación se detallan los paneles específicos que se pueden crear para cada una de las ideas de dashboards, utilizando el archivo `nics_demo_flat.json` como fuente de datos en Grafana Infinity.

---

## 1. Resumen de la Postura de Ciberseguridad

### Paneles:

1.  **Puntuación General de la Función (5 Paneles tipo Medidor)**
    *   **Tipo de Panel:** Medidor (Gauge)
    *   **Datos:** `function_score`
    *   **Configuración:** Crear un panel para cada una de las 5 funciones (`IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND`, `RECOVER`).
        *   **Consulta:** Filtrar por el nombre de la función (ej. `function == "IDENTIFY (ID)"`) y seleccionar el campo `function_score`.
        *   **Visualización:** Configurar umbrales de color: Rojo (0-60), Amarillo (61-80), Verde (81-100).

2.  **Puntuaciones por Categoría (Gráfico de Barras)**
    *   **Tipo de Panel:** Gráfico de Barras (Bar Chart)
    *   **Datos:** `category`, `category_score`
    *   **Configuración:**
        *   **Consulta:** Seleccionar los campos `category` y `category_score`. Agrupar por `category` para asegurarse de que cada barra representa una categoría única.
        *   **Visualización:** Usar el campo `category` en el eje X y `category_score` en el eje Y. Se puede agrupar por `function` para colorear las barras según la función a la que pertenecen.

3.  **Tabla de Puntuaciones (Tabla)**
    *   **Tipo de Panel:** Tabla (Table)
    *   **Datos:** `function`, `category`, `subcategory`, `category_score`, `subcategory_score`
    *   **Configuración:**
        *   **Consulta:** Seleccionar todos los campos relevantes.
        *   **Visualización:** Mostrar las columnas en el orden deseado. Permitir ordenar por `category_score` y `subcategory_score` para identificar rápidamente las áreas de menor rendimiento. Usar umbrales de color en las celdas de puntuación para una rápida identificación visual.

---

## 2. Análisis de Madurez por Dominio

### Paneles:

1.  **Radar de Madurez por Categoría (Gráfico de Radar)**
    *   **Tipo de Panel:** Gráfico de Radar (Radar Chart) o similar (Polystat).
    *   **Datos:** `policy_score`, `process_score`, `implementation_score`, `measured_score`, `managed_score`
    *   **Configuración:**
        *   **Consulta:** Seleccionar una `category` específica (se puede usar una variable de Grafana para permitir al usuario elegir la categoría).
        *   **Visualización:** Cada eje del radar representará un nivel de madurez (Política, Proceso, etc.), y el valor será la puntuación promedio para esa categoría.

2.  **Mapa de Calor de Madurez (Mapa de Calor)**
    *   **Tipo de Panel:** Mapa de Calor (Heatmap)
    *   **Datos:** `subcategory`, niveles de madurez y sus puntuaciones.
    *   **Configuración:**
        *   **Consulta:** Seleccionar `subcategory` y todas las columnas de puntuación de madurez (`policy_score`, `process_score`, etc.).
        *   **Visualización:** El eje Y serán las `subcategory`, el eje X los 5 niveles de madurez, y el color de la celda representará la puntuación. Esto permite ver rápidamente qué aspectos de la madurez son más débiles en general.

3.  **Tabla Detallada de Madurez (Tabla)**
    *   **Tipo de Panel:** Tabla (Table)
    *   **Datos:** `category`, `subcategory`, y todas las columnas de madurez (`policy_maturity`, `policy_score`, etc.).
    *   **Configuración:**
        *   **Consulta:** Seleccionar todos los campos relevantes.
        *   **Visualización:** Mostrar tanto el nivel de madurez (ej. "Fully Compliant") como la puntuación. Usar umbrales de color en las celdas de puntuación.

---

## 3. Análisis de Esfuerzo vs. Puntuación (Quick Wins)

### Paneles:

1.  **Gráfico de Dispersión de Esfuerzo vs. Puntuación (Gráfico de Dispersión)**
    *   **Tipo de Panel:** Gráfico de Dispersión (Scatter Plot)
    *   **Datos:** `estimated_level_of_effort_in_hours`, `subcategory_score`, `subcategory`
    *   **Configuración:**
        *   **Consulta:** Seleccionar los campos mencionados.
        *   **Visualización:** Eje X: `estimated_level_of_effort_in_hours`. Eje Y: `subcategory_score`. Cada punto es una `subcategory`. Los puntos en la esquina inferior izquierda son los "quick wins".

2.  **Tabla de Prioridades (Tabla)**
    *   **Tipo de Panel:** Tabla (Table)
    *   **Datos:** `subcategory`, `subcategory_score`, `estimated_level_of_effort_in_hours`
    *   **Configuración:**
        *   **Consulta:** Seleccionar los campos y añadir una columna calculada para el "Índice de Prioridad" (`subcategory_score` / `estimated_level_of_effort_in_hours`).
        *   **Visualización:** Ordenar la tabla por el índice de prioridad de forma ascendente para ver las tareas más eficientes primero.

---

## 4. Vista del Registro de Riesgos

### Paneles:

1.  **Tabla de Riesgos Registrados (Tabla)**
    *   **Tipo de Panel:** Tabla (Table)
    *   **Datos:** `function`, `category`, `subcategory`, `risk_register`
    *   **Configuración:**
        *   **Consulta:** Filtrar donde `risk_register` no sea nulo.
        *   **Visualización:** Mostrar las columnas para identificar claramente dónde se han registrado los riesgos.

2.  **Contador de Riesgos Totales (Estadística)**
    *   **Tipo de Panel:** Estadísticas (Stat / Singlestat)
    *   **Datos:** Conteo de `risk_register`
    *   **Configuración:**
        *   **Consulta:** Contar el número de registros donde `risk_register` no es nulo.
        *   **Visualización:** Mostrar un número grande y claro.

3.  **Riesgos por Función (Gráfico de Barras)**
    *   **Tipo de Panel:** Gráfico de Barras (Bar Chart)
    *   **Datos:** `function`, conteo de `risk_register`
    *   **Configuración:**
        *   **Consulta:** Agrupar por `function` y contar los registros donde `risk_register` no es nulo.
        *   **Visualización:** Mostrar el número de riesgos por cada función de ciberseguridad.

---

## 5. Estado de Cumplimiento y Artefactos

### Paneles:

1.  **Estado de Artefactos (Gráfico de Tarta)**
    *   **Tipo de Panel:** Gráfico de Tarta (Pie Chart)
    *   **Datos:** `artifacts_placed_in_folder`
    *   **Configuración:**
        *   **Consulta:** Agrupar por `artifacts_placed_in_folder` y contar los valores (`Y` vs. `N`/nulo).
        *   **Visualización:** Mostrar el porcentaje de subcategorías que tienen la documentación necesaria.

2.  **Tabla de Brechas de Artefactos (Tabla)**
    *   **Tipo de Panel:** Tabla (Table)
    *   **Datos:** `function`, `category`, `subcategory`, `artifacts_needed`
    *   **Configuración:**
        *   **Consulta:** Filtrar donde `artifacts_placed_in_folder` sea 'N' o nulo.
        *   **Visualización:** Listar las áreas donde falta documentación, junto con la descripción de lo que se necesita (`artifacts_needed`).

3.  **Contador de Artefactos Faltantes (Estadística)**
    *   **Tipo de Panel:** Estadísticas (Stat / Singlestat)
    *   **Datos:** Conteo de `artifacts_placed_in_folder`
    *   **Configuración:**
        *   **Consulta:** Contar el número de registros donde `artifacts_placed_in_folder` es 'N' o nulo.
        *   **Visualización:** Mostrar un número grande para un impacto visual rápido.

---

## 6. Explorador Detallado de Subcategorías

### Paneles:

1.  **Tabla Maestra de Subcategorías (Tabla)**
    *   **Tipo de Panel:** Tabla (Table)
    *   **Datos:** Todos los campos del JSON aplanado.
    *   **Configuración:**
        *   **Consulta:** Seleccionar todos los campos (`*`).
        *   **Visualización:** Este panel es para la exploración. Habilitar la funcionalidad de búsqueda y filtrado de la tabla de Grafana. El usuario podrá escribir para buscar en cualquier campo y usar las opciones de filtrado de la tabla para análisis ad-hoc. Se pueden usar "overrides" para colorear celdas de puntuación o formatear texto.
