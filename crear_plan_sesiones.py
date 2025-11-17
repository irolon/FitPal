from data_base.Conexion import Conexion
from DAO.Plan_sesion_DAO import PlanSesionDAO
from DAO.Sesiones_DAO import SesionesDAO
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO
from Model.Plan_Sesion import PlanSesion
from Model.Sesion import Sesion

def crear_planes_sesion():
    # Crear conexión a la base de datos
    conexion_wrapper = Conexion('data_base/db_fitpal.db')
    
    # Crear instancias de DAO
    plan_sesion_dao = PlanSesionDAO(conexion_wrapper.conexion)
    sesion_dao = SesionesDAO(conexion_wrapper.conexion)
    plan_dao = PlanEntrenamientoDAO(conexion_wrapper.conexion)
    
    # Crear las tablas si no existen
    sesion_dao.create_table()
    plan_sesion_dao.create_table()
    
    # Verificar si ya existen sesiones
    sesiones_existentes = sesion_dao.list()
    print(f"Sesiones existentes: {len(sesiones_existentes)}")
    
    if len(sesiones_existentes) < 5:
        # Crear sesiones de ejemplo
        print("Creando sesiones de ejemplo...")
        sesiones_data = [
            {"nombre": "Sesión de Calentamiento", "descripcion": "Ejercicios de calentamiento y estiramientos"},
            {"nombre": "Sesión de Fuerza", "descripcion": "Entrenamiento con pesas y resistencia"},
            {"nombre": "Sesión Cardiovascular", "descripcion": "Ejercicios aeróbicos y cardio"},
            {"nombre": "Sesión de Flexibilidad", "descripcion": "Yoga y estiramientos profundos"},
            {"nombre": "Sesión HIIT", "descripcion": "Entrenamiento de alta intensidad"},
        ]

        for sesion_data in sesiones_data:
            sesion = Sesion(
                nombre=sesion_data["nombre"],
                descripcion=sesion_data["descripcion"]
            )
            sesion_id = sesion_dao.create(sesion)
            if sesion_id:
                print(f"✓ Sesión '{sesion_data['nombre']}' creada con ID: {sesion_id}")
    
    # Obtener sesiones y planes actualizados
    sesiones = sesion_dao.list()
    planes = plan_dao.list()
    
    print(f"\nSesiones disponibles: {len(sesiones)}")
    print(f"Planes disponibles: {len(planes)}")
    
    # Verificar si ya existen planes de sesión
    planes_sesion_existentes = plan_sesion_dao.list()
    print(f"Planes de sesión existentes: {len(planes_sesion_existentes)}")
    
    if len(planes_sesion_existentes) == 0:
        print("\nCreando planes de sesión...")
        plan_sesiones_creados = 0
        
        # Tomar solo los primeros 10 planes para evitar duplicados
        planes_a_usar = planes[:10]
        sesiones_a_usar = sesiones[:3]  # Primeras 3 sesiones
        
        for plan in planes_a_usar:
            print(f"Procesando plan ID: {plan.id}")
            for orden, sesion in enumerate(sesiones_a_usar, 1):
                try:
                    plan_sesion_id = plan_sesion_dao.create(plan.id, sesion.id, orden)
                    if plan_sesion_id:
                        plan_sesiones_creados += 1
                        print(f"✓ Plan-Sesión creado: Plan {plan.id} -> Sesión {sesion.id} (Orden {orden})")
                    else:
                        print(f"✗ Error al crear plan-sesión para Plan {plan.id} y Sesión {sesion.id}")
                except Exception as e:
                    print(f"✗ Excepción al crear plan-sesión: {e}")
        
        print(f"\nTotal plan-sesiones creados: {plan_sesiones_creados}")
    else:
        print("Ya existen planes de sesión. Saltando creación.")
    
    # Verificar resultados por cliente
    print("\n=== Verificando planes de sesión por cliente ===")
    for cliente_id in [2, 3, 4]:  # Primeros 3 clientes
        planes_sesion_cliente = plan_sesion_dao.read_by_cliente_id(cliente_id)
        print(f"Cliente {cliente_id}: {len(planes_sesion_cliente)} planes de sesión")
        for ps in planes_sesion_cliente[:3]:  # Solo mostrar primeros 3
            print(f"  - {ps.mostrarDatos()}")
    
    # Cerrar conexión
    conexion_wrapper.conexion.close()
    print("\nProceso completado.")

if __name__ == "__main__":
    crear_planes_sesion()