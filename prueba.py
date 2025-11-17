from datetime import date, timedelta
from data_base.Conexion import Conexion
from DAO.Plan_entrenamiento_DAO import PlanEntrenamientoDAO
from DAO.Cliente_DAO import ClienteDAO
from DAO.Usuario_DAO import UsuarioDAO
from DAO.Plan_sesion_DAO import PlanSesionDAO
from DAO.Sesiones_DAO import SesionesDAO
from Model.Plan_entrenamiento import PlanEntrenamiento
from Model.Usuario import Usuario
from Model.Cliente import Cliente
from Model.Plan_Sesion import PlanSesion
from Model.Sesion import Sesion

def main():
    # Crear conexión a la base de datos
    conexion_wrapper = Conexion('data_base/db_fitpal.db')

    # Crear instancias de DAO pasando el objeto de conexión SQLite3
    plan_dao = PlanEntrenamientoDAO(conexion_wrapper.conexion)
    cliente_dao = ClienteDAO(conexion_wrapper.conexion)
    usuario_dao = UsuarioDAO(conexion_wrapper.conexion)
    plan_sesion_dao = PlanSesionDAO(conexion_wrapper.conexion)
    sesion_dao = SesionesDAO(conexion_wrapper.conexion)

    # Crear las tablas necesarias
    print("Creando tablas...")
    usuario_dao.create_table()
    cliente_dao.create_table()
    plan_dao.create_table()
    sesion_dao.create_table()
    plan_sesion_dao.create_table()

    # Verificar si existen usuarios y clientes
    print("Verificando usuarios y clientes existentes...")
    usuarios_existentes = usuario_dao.list()
    clientes_existentes = cliente_dao.list()

    # Obtener clientes existentes que sean de tipo 'cliente'
    clientes_usuario = [u for u in usuarios_existentes if u.rol == 'cliente']
    
    if not clientes_existentes or len(clientes_existentes) < 10:
        print("Creando usuarios y clientes de ejemplo...")
        
        # Crear un administrador si no existe
        admin_existente = [u for u in usuarios_existentes if u.rol == 'administrador']
        if not admin_existente:
            admin = Usuario("Admin", "Sistema", "admin@fitness.com", "admin123", "administrador")
            admin_id = usuario_dao.create(admin)
            print(f"Administrador creado con ID: {admin_id}")
        else:
            admin_id = admin_existente[0].id
            print(f"Usando administrador existente con ID: {admin_id}")
        
        # Crear 10 usuarios cliente de ejemplo
        usuarios_cliente_data = [
            ("Juan", "Pérez", "juan.perez@email.com"),
            ("María", "González", "maria.gonzalez@email.com"),
            ("Carlos", "Rodríguez", "carlos.rodriguez@email.com"),
            ("Ana", "Martínez", "ana.martinez@email.com"),
            ("Luis", "García", "luis.garcia@email.com"),
            ("Carmen", "López", "carmen.lopez@email.com"),
            ("Miguel", "Hernández", "miguel.hernandez@email.com"),
            ("Laura", "Jiménez", "laura.jimenez@email.com"),
            ("Pedro", "Ruiz", "pedro.ruiz@email.com"),
            ("Sofia", "Díaz", "sofia.diaz@email.com"),
        ]
        
        clientes_ids = []
        for i, (nombre, apellido, email) in enumerate(usuarios_cliente_data):
            # Crear usuario cliente
            usuario_cliente = Usuario(nombre, apellido, email, "password123", "cliente")
            usuario_id = usuario_dao.create(usuario_cliente)
            
            if usuario_id:
                # Crear cliente asociado
                cliente = Cliente(
                    nombre="", apellido="", correo="", contrasena="",
                    dni=f"1234567{i:02d}",
                    edad=20 + i,
                    fecha_inicio=date.today()
                )
                cliente_creado = cliente_dao.create(usuario_id, cliente)
                if cliente_creado:
                    clientes_ids.append(usuario_id)
                    print(f"✓ Usuario y cliente creados: {nombre} {apellido} (ID: {usuario_id})")
                else:
                    print(f"✗ Error al crear cliente para usuario ID: {usuario_id}")
            else:
                print(f"✗ Error al crear usuario: {nombre} {apellido}")
        
        print(f"Clientes creados: {len(clientes_ids)}")
    else:
        # Usar clientes existentes
        clientes_ids = [cliente[0] for cliente in clientes_existentes[:10]]
        print(f"Usando clientes existentes: {clientes_ids}")

    # Verificar que tenemos suficientes clientes
    if len(clientes_ids) < 10:
        print(f"Solo hay {len(clientes_ids)} clientes disponibles. Necesitamos 10.")
        conexion_wrapper.conexion.close()
        return

    # Datos de ejemplo para los planes de entrenamiento
    planes_data = [
        {
            'nombre': 'Plan de Fuerza Básico',
            'frecuencia': 3,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=30)
        },
        {
            'nombre': 'Plan Cardiovascular',
            'frecuencia': 4,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=45)
        },
        {
            'nombre': 'Plan Pérdida de Peso',
            'frecuencia': 5,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=60)
        },
        {
            'nombre': 'Plan Tonificación',
            'frecuencia': 3,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=35)
        },
        {
            'nombre': 'Plan Resistencia',
            'frecuencia': 4,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=40)
        },
        {
            'nombre': 'Plan Principiante',
            'frecuencia': 2,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=30)
        },
        {
            'nombre': 'Plan Avanzado',
            'frecuencia': 6,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=90)
        },
        {
            'nombre': 'Plan Funcional',
            'frecuencia': 3,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=50)
        },
        {
            'nombre': 'Plan Híbrido',
            'frecuencia': 4,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=75)
        },
        {
            'nombre': 'Plan Especializado',
            'frecuencia': 5,
            'fecha_inicio': date.today(),
            'fecha_fin': date.today() + timedelta(days=120)
        }
    ]

    print("\n=== Creando 10 planes de entrenamiento ===")
    
    # Crear los 10 planes de entrenamiento
    planes_creados = 0
    for i, plan_data in enumerate(planes_data):
        # Crear el objeto PlanEntrenamiento
        plan = PlanEntrenamiento(
            administrador_id=1,  # Asumiendo que existe un administrador con ID 1
            cliente_id=clientes_ids[i],
            nombre=plan_data['nombre'],
            frecuencia=plan_data['frecuencia'],
            fecha_inicio=plan_data['fecha_inicio'],
            fecha_fin=plan_data['fecha_fin']
        )
        
        # Insertar en la base de datos
        plan_id = plan_dao.create(
            administrador_id=1,
            cliente_id=clientes_ids[i],
            p=plan
        )
        
        if plan_id:
            planes_creados += 1
            print(f"✓ Plan '{plan_data['nombre']}' creado con ID: {plan_id} para cliente ID: {clientes_ids[i]}")
        else:
            print(f"✗ Error al crear el plan '{plan_data['nombre']}' para cliente ID: {clientes_ids[i]}")

    print(f"\n=== Resumen ===")
    print(f"Planes creados exitosamente: {planes_creados}/10")

    # Crear sesiones de ejemplo
    print("\n=== Creando sesiones de ejemplo ===")
    sesiones_data = [
        {"nombre": "Sesión de Calentamiento", "descripcion": "Ejercicios de calentamiento y estiramientos"},
        {"nombre": "Sesión de Fuerza", "descripcion": "Entrenamiento con pesas y resistencia"},
        {"nombre": "Sesión Cardiovascular", "descripcion": "Ejercicios aeróbicos y cardio"},
        {"nombre": "Sesión de Flexibilidad", "descripcion": "Yoga y estiramientos profundos"},
        {"nombre": "Sesión HIIT", "descripcion": "Entrenamiento de alta intensidad"},
    ]

    sesiones_ids = []
    for sesion_data in sesiones_data:
        sesion = Sesion(
            nombre=sesion_data["nombre"],
            descripcion=sesion_data["descripcion"]
        )
        sesion_id = sesion_dao.create(sesion)
        if sesion_id:
            sesiones_ids.append(sesion_id)
            print(f"✓ Sesión '{sesion_data['nombre']}' creada con ID: {sesion_id}")
        else:
            print(f"✗ Error al crear sesión '{sesion_data['nombre']}'")

    # Crear planes de sesión (relacionar planes con sesiones)
    print("\n=== Creando planes de sesión ===")
    planes_en_db = plan_dao.list()
    plan_sesiones_creados = 0

    if planes_en_db and sesiones_ids:
        for i, plan in enumerate(planes_en_db):
            # Asignar 2-3 sesiones por plan de entrenamiento
            sesiones_para_plan = sesiones_ids[:3]  # Primeras 3 sesiones para cada plan
            
            for orden, sesion_id in enumerate(sesiones_para_plan, 1):
                plan_sesion = PlanSesion(
                    plan_id=plan.id,
                    sesion_id=sesion_id,
                    orden=orden
                )
                
                plan_sesion_id = plan_sesion_dao.create(plan.id, sesion_id, orden)
                if plan_sesion_id:
                    plan_sesiones_creados += 1
                    print(f"✓ Plan-Sesión creado: Plan {plan.id} -> Sesión {sesion_id} (Orden {orden})")
                else:
                    print(f"✗ Error al crear plan-sesión para Plan {plan.id} y Sesión {sesion_id}")

    print(f"\nPlan-sesiones creados: {plan_sesiones_creados}")

    # Verificar los planes creados
    print("\n=== Planes de entrenamiento en la base de datos ===")
    if planes_en_db:
        for plan in planes_en_db:
            print(plan.mostrarDatos())
    else:
        print("No se encontraron planes de entrenamiento.")

    # Verificar planes de sesión por cliente
    print("\n=== Verificando planes de sesión por cliente ===")
    for cliente_id in clientes_ids[:3]:  # Solo mostrar primeros 3 clientes
        planes_sesion_cliente = plan_sesion_dao.read_by_cliente_id(cliente_id)
        print(f"Cliente {cliente_id}: {len(planes_sesion_cliente)} planes de sesión")
        for ps in planes_sesion_cliente:
            print(f"  - {ps.mostrarDatos()}")

    # Cerrar conexión
    conexion_wrapper.conexion.close()
    print("\nProceso completado.")

if __name__ == "__main__":
    main()