# Arquitectura del Ecosistema Pime IA

Este documento define la estructura técnica y lógica de **Pime IA**, diseñado para que Oscar Patiño orqueste sus empresas (Desafia, Ingeniería Civil) con el apoyo de IA.

## Diagrama Conceptual

```mermaid
graph TD
    User[Oscar - Arquitecto] -->|Dirección & Comandos| AI[Antigravity / Jessy (Orquestador IA)]
    
    subgraph "Núcleo Pime IA"
        AI -->|Genera & Ejecuta| Scripts[Scripts Python (Lógica)]
        AI -->|Consulta| DB[(Datos / JSON / SQL)]
    end
    
    subgraph "Módulos de Negocio"
        Scripts -->|Gestiona| ModIng[Módulo Ingeniería]
        Scripts -->|Gestiona| ModFin[Módulo Financiero]
        Scripts -->|Gestiona| ModConst[Módulo Construcción]
    end
    
    subgraph "Salidas & Entregables"
        ModIng --> Reports[Reportes & Memorias]
        ModFin --> Dashboards[Tableros Control]
        ModConst --> Plans[Planos & Cronogramas]
    end
```

## Componentes Principales

### 1. El Orquestador (La Mente)
*   **Rol:** Interpreta las necesidades de Oscar y las traduce en tareas técnicas.
*   **Tecnología:** Modelos de Lenguaje (Gemini) integrados en el entorno de desarrollo (VS Code / Antigravity).

### 2. Los Ejecutores (Los Brazos)
*   **Scripts Python:** Pequeños programas especializados.
    *   Ejemplo: `calcular_wind_load.py` (Ingeniería) o `reporte_gastos.py` (Finanzas).
*   **Filosofía Modular:** Cada script hace UNA cosa bien hecha.

### 3. La Memoria (Los Datos)
*   **Fase 1:** Archivos JSON y Excel. Fáciles de leer y editar manualmente si es necesario.
*   **Fase 2:** Base de datos SQL estructurada cuando el volumen crezca.

## Flujo de Trabajo (Workflow)
1.  **Oscar** define una necesidad: "Necesito ver el costo por m2 del proyecto Box Salitre".
2.  **Oscar/Santiago** invocan el script correspondiente (o le piden a Antigravity que lo cree).
3.  **El Sistema** lee los datos de los proyectos, calcula y genera un reporte.
4.  **Oscar** toma decisiones basadas en el reporte.
