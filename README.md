# Structural Math Calculator

Aplicación web educativa y visual para matemática estructural. La interfaz permite elegir un módulo de cálculo, ingresar datos, obtener resultados con unidades, ver el procedimiento matemático completo y revisar diagramas o representaciones estructurales sin depender de librerías externas.

## Funcionalidades implementadas

- Esfuerzo normal: `sigma = F / A`
- Deformación unitaria: `epsilon = deltaL / L`
- Ley de Hooke con despeje de `sigma`, `E` o `epsilon`
- Momento: `M = F * d`
- Vigas simplemente apoyadas con:
  - carga puntual
  - carga distribuida uniforme
  - reacciones en apoyos
  - diagrama de carga
  - diagrama de cortante
  - diagrama de momento flector
- Deflexión para carga puntual centrada: `delta = (P * L^3) / (48 * E * I)`
- Momento de inercia para:
  - rectángulo
  - círculo
  - triángulo
- Conversión de unidades:
  - `N <-> kN`
  - `mm <-> cm <-> m`
  - `Pa <-> MPa <-> GPa`
- Modo aprendizaje con:
  - teoría breve
  - explicación de variables
  - contexto de uso
  - ejemplo resuelto automáticamente

## Stack

- Frontend: HTML, CSS y JavaScript modular
- Visualización: SVG y Canvas nativos
- Servidor local: Python estándar con `http.server`

## Estructura del proyecto

```text
.
|-- main.py
|-- README.md
|-- README_AI.md
`-- web
    |-- index.html
    |-- styles.css
    `-- js
        |-- app.js
        |-- engineering.js
        |-- modules-data.js
        `-- visualizations.js
```

## Instalación y ejecución

1. Asegura tener Python 3 instalado.
2. Desde la raíz del proyecto ejecuta:

```bash
python3 main.py
```

3. Abre en el navegador:

```text
http://localhost:8000
```

## Uso básico

1. Selecciona un módulo en el panel lateral.
2. Completa los campos del formulario.
3. Presiona `Calcular`.
4. Usa `Mostrar desarrollo` para ver u ocultar:
   - Fórmula general
   - Sustitución de valores
   - Resolución paso a paso
   - Resultado final
   - Interpretación del resultado
5. Revisa la visualización inferior y el bloque de `Modo aprendizaje`.

## Diseño técnico

- La app está preparada para crecer a partir de metadatos por módulo en [`modules-data.js`](/workspaces/RDM-proyects/web/js/modules-data.js).
- La lógica de ingeniería está centralizada en [`engineering.js`](/workspaces/RDM-proyects/web/js/engineering.js).
- Las visualizaciones están desacopladas en [`visualizations.js`](/workspaces/RDM-proyects/web/js/visualizations.js).
- La UI principal y los formularios dinámicos viven en [`app.js`](/workspaces/RDM-proyects/web/js/app.js).

## Próximas ampliaciones sugeridas

- Análisis de armaduras
- Método de nodos
- Método de secciones
- Pórticos
- Más tipos de apoyos
- Más tipos de carga
- Secciones compuestas
- Exportación de reportes de cálculo

## Limitaciones actuales

- Los diagramas de vigas cubren la versión base para vigas simplemente apoyadas.
- La deflexión implementada corresponde al caso clásico de carga puntual centrada.
- El momento de inercia de secciones compuestas y perfiles reales aún no está incluido.
- No hay persistencia de cálculos ni exportación a PDF en esta versión base.
