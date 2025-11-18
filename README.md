FITPAL – Aplicación de
Entrenamiento Personalizado
PARCIAL II – Grupo 10

Asignatura
    • Análisis y Metodología de Sistemas
Comisión
    • ACN4BV
Docente
    • Gionnelly Vielza Durán
Integrantes
    • Ignacio Rolón
    • Pablo Queimaliños
    • Martín Bianco



    
Descripción del Proyecto:
FitPal es una aplicación innovadora de entrenamiento personalizado diseñada para acompañar a los usuarios en el cumplimiento de sus objetivos de fitness, brindando planes de ejercicio a medida y fomentando la motivación mediante dinámicas de gamificación. La propuesta busca no solo ofrecer rutinas de entrenamiento, sino también construir una experiencia integral en la que el usuario sienta que tiene un entrenador digital en todo momento.
Alcance:
El alcance del proyecto comprende el diseño, desarrollo e implementación de una aplicación de entrenamiento personalizado que permitirá a los usuarios acceder a planes de ejercicio adaptados a sus objetivos y características individuales, así como a un sistema de seguimiento y motivación basado en la gamificación.
La aplicación contará con dos tipos de usuarios:
    • Administrador: encargado de gestionar la plataforma mediante un panel que le permitirá realizar operaciones para crear, consultar, actualizar y eliminar, sobre los usuarios, planes de entrenamiento, sesiones y ejercicios. Tendrá la capacidad de asignar planes a clientes y mantener actualizada la base de datos.
    • Cliente: podrá registrarse en la aplicación, configurar su perfil (datos personales, edad, peso, objetivos) y acceder a los planes asignados por el administrador. Además, tendrá disponible un sistema para registrar su
progreso, marcar sesiones completadas, visualizar estadísticas y recibir recompensas por logros alcanzados.
El proyecto incluye:
    • Gestión de Usuarios: alta, modificación y baja de clientes y administradores.
    • Gestión de Ejercicios y Planes: creación de un catálogo de ejercicios con series, repeticiones, tiempos y categorías, así como la estructuración de planes y
sesiones de entrenamiento.
    • Seguimiento de Progreso: registro del cumplimiento de sesiones, visualización de estadísticas semanales y mensuales, historial de avances e indicadores de rendimiento.
    • Gamificación y Motivación: implementación de logros, niveles y puntajes que fomenten la constancia y el compromiso del usuario con sus objetivos.
    • Base de Datos Relacional: diseño e implementación de un modelo que garantice la integridad de la información y las relaciones entre usuarios, planes, sesiones y progreso.
    • Control de Versiones: administración del código mediante GitHub, con ramas para desarrollo, producción y versiones etiquetadas.

Enfoque del Proyecto:
El desarrollo se centrará en tres ejes fundamentales:
Interfaz de Usuario Amigable e Intuitiva

        ◦ El diseño buscará simplicidad y accesibilidad, garantizando que tanto usuarios principiantes como avanzados puedan navegar sin dificultades.
        ◦ Se implementarán vistas claras y organizadas para la selección de planes, seguimiento de progreso y visualización de logros.
        ◦ El cliente contará con un perfil personalizable que mostrará sus datos básicos, objetivos actuales y un resumen de su progreso.

Gestión Administrativa Eficiente

        ◦ Se desarrollará un módulo de administración que permita a los administradores mantener la base de datos actualizada.
        ◦ Los planes de ejercicio podrán ser editados o eliminados en función de su vigencia y efectividad.

Motivación a través de la Gamificación

        ◦ Se incorporarán recompensas por completar planes, alcanzar objetivos o superar desafíos.
        ◦ El sistema ofrecerá notificaciones y recordatorios que inviten al usuario a mantener la constancia en sus entrenamientos.
Modelo de Datos
Con el objetivo de estructurar la información de manera eficiente y garantizar la correcta administración de usuarios, planes y ejercicios, diseñamos el diagrama entidad–relación (DER) de la base de datos de FitPal.
Este diagrama refleja la organización de las principales entidades del sistema y sus relaciones:
    • Usuarios: almacena los datos de clientes y administradores, incluyendo información personal, credenciales de acceso, rol asignado y estado de la cuenta.
    • Planes de Entrenamiento: contiene la información de los programas creados por los administradores, asociados a usuarios específicos.
    • Sesiones: representan la estructura de cada plan, detallando qué ejercicios corresponden a cada etapa del entrenamiento.
    • Ejercicios: catálogo con todos los ejercicios disponibles, clasificados por categoría (fuerza, aeróbico, recuperación, descanso), incluyendo repeticiones, series y tiempo estimado.
    • Progreso del Usuario: registra la evolución individual de cada cliente en función de logros, puntajes y niveles alcanzados.
    • Logros: elementos de gamificación que identifican objetivos cumplidos o desafíos superados por los usuarios.
A continuación, se presenta el diagrama lógico elaborado:



Diagrama de Flujo – Inicio de Sesión
Elaboramos el diagrama de flujo que describe el proceso de inicio de sesión dentro de la aplicación. Este diagrama permite visualizar de manera detallada los pasos que siguen los usuarios al acceder a la plataforma, así como las validaciones necesarias para garantizar un acceso seguro y controlado.
El flujo contempla las siguientes etapas:
    1. Ingreso de credenciales: el usuario introduce su correo electrónico y contraseña en el formulario de acceso.
    2. Verificación del correo electrónico: el sistema valida si el correo existe en la base de datos.
        ◦ En caso de error, se notifica que el correo es incorrecto.
    3. Estado del usuario: se verifica si la cuenta está activa.
        ◦ Si el usuario se encuentra inactivo, se muestra el correspondiente mensaje de restricción.
    4. Validación de la contraseña: se comprueba que la clave ingresada coincida con la almacenada en la base de datos.
        ◦ Si es incorrecta, se notifica el error.
    5. Determinación del rol: el sistema identifica si el usuario que accede es
administrador o cliente.
        ◦ Administrador: accede al panel de gestión, con funciones CRUD sobre usuarios, planes y ejercicios.
        ◦ Cliente: accede a su perfil personal, donde puede consultar sus rutinas, registrar progresos y visualizar logros.
El diagrama garantiza los distintos escenarios posibles en el inicio de sesión, incluyendo validaciones de seguridad y control de permisos.
A continuación, se presenta el diagrama desarrollado


Implementación en Código
Actualmente, el proyecto ya cuenta con un primer desarrollo, el cual fue subido y gestionado en un repositorio de GitHub, lo que permite mantener control de versiones y trabajo en equipo.
Gestión en GitHub
    • Se han creado tres ramas para organizar el flujo de trabajo:
    • Master: rama principal y estable.
    • Desarrollo: destinada a la incorporación de nuevas funcionalidades y pruebas.
    • Producción: versión preparada para despliegue.
    • Se creó además un tag v1.0.0, que marca la primera versión estable del sistema.
Clases Implementadas Usuario
    • Clase abstracta que define los atributos y métodos básicos de cualquier usuario del sistema (nombre, apellido, correo, contraseña, rol).
    • Contiene el método abstracto mostrarDatos(), que es implementado por las clases hijas.
Cliente
    • Hereda de Usuario.
    • Atributos adicionales: DNI, edad, fecha_inicio.
    • Método mostrarDatos(): retorna los datos generales del usuario, junto con información específica del cliente
Administrador
    • Hereda de Usuario.
    • Atributos adicionales: activo, fecha_alta.
    • Método mostrarDatos(): retorna los datos generales del usuario, indicando además el estado (activo/inactivo) y la fecha de alta.
Main
    • Archivo principal que instancia objetos de las clases Cliente y Administrador.
    • Permite probar la creación de usuarios y la ejecución del método mostrarDatos() en cada caso.



Actualización del proyecto al 18/11/2025

Estado actual del proyecto:
- El proyecto cuenta con dos perfiles de usuarios funcionando, administrador y cliente.

El perfil de Administrador tiene la funcionalidad de Alta, Baja y Modificación completas de Ejercicios, donde se puede registrar Categoría, nombre, descripción, repeticiones, series y tiempo de descanso en segundos.

Esos ejercicios, compondrán las sesiones de entrenamiento y desde este perfil podemos también hacer un Alta, Baja y Modificación de Sesiones. Allí registramos nombre de la sesión, descripción y ejercicios que la componen.

Finalmente, estas sesiones de entrenamiento componen a su vez a Planes de entrenamiento, los cuales son creados por usuarios administradores y asignados a usuarios clientes, indicando fecha de inicio, fecha de fin, periodicidad y sesiones de entrenamiento que la componen.

Por último, para esta entrega, el perfil de Admin cuenta también con un ABM de Usuarios.

Por otro lado, para el perfil cliente, lo que vamos a encontrar en esta instancia funcionando es la posibilida de ver los planes de entrenamiento que le fueron asignados así como también las sesiones de entrenamiento que conforman esos planes, pudiendo indicar en las mismas si se encuentran pendientes o si fueron completadas.

Por cuestiones de tiempo y complejidad de las funcionalidades, lo que respecta a gamificación queda por fuera de esta instancia de entrega. Es decir, aquello que tiene que ver con asignar puntajes para los clientes en base a las sesiones de entrenamiento completadas o la posiblidad de generar logros y objetivos específicos. 

Además, quedan también para siguientes mejoras al proyecto, ampliar la información disponible para clientes y administradores sobre métricas y seguimiento, así como también lo que refiere a la automatización de asignación de planes o sugerencias de entrenamiento.

Por último, para esta entrega incorporamos también pruebas unitarias de las funcionalidades de login, CRUD de ejercicos y CRUD de sesiones.


