import json
import os
from datetime import datetime

# --- CONFIGURACIÓN ---
ARCHIVO_DATOS = "proyectos_db.json"

def cargar_proyectos():
    """Carga los proyectos existentes desde el archivo JSON."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar la base de datos: {e}")
        return []

def guardar_proyecto(proyecto):
    """Guarda un nuevo proyecto en la base de datos."""
    proyectos = cargar_proyectos()
    proyectos.append(proyecto)
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(proyectos, f, indent=4, ensure_ascii=False)
    print("✅ Proyecto guardado exitosamente.")

def crear_proyecto():
    """Interfaz para pedir datos al usuario (Oscar/Santiago)."""
    print("\n--- NUEVO PROYECTO PIME IA ---")
    nombre = input("Nombre del Proyecto: ")
    cliente = input("Cliente: ")
    
    while True:
        try:
            presupuesto = float(input("Presupuesto (COP): "))
            break
        except ValueError:
            print("❌ Por favor ingrese un número válido.")

    categoria = input("Categoría (Civil/Tecnología/Consultoría): ")

    nuevo_proyecto = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"), # ID único basado en fecha/hora
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nombre": nombre,
        "cliente": cliente,
        "presupuesto": presupuesto,
        "categoria": categoria,
        "estado": "Activo"
    }
    
    guardar_proyecto(nuevo_proyecto)

def listar_proyectos():
    """Muestra los proyectos registrados."""
    proyectos = cargar_proyectos()
    print("\n--- LISTADO DE PROYECTOS ---")
    if not proyectos:
        print("No hay proyectos registrados aún.")
    
    for p in proyectos:
        print(f"[{p['id']}] {p['nombre']} - {p['cliente']} (${p['presupuesto']:,.0f})")

def menu_principal():
    while True:
        print("\n--- SISTEMA GESTIÓN PIME IA ---")
        print("1. Registrar Nuevo Proyecto")
        print("2. Ver Proyectos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_proyecto()
        elif opcion == "2":
            listar_proyectos()
        elif opcion == "3":
            print("¡Hasta luego Arquitecto!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
