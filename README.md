# 🏋️‍♂️ FitPal – Entrenador Digital Personalizado

FitPal es una plataforma web de entrenamiento que combina planes personalizados, seguimiento del progreso, registro de sesiones y un panel administrativo completo.  
Su objetivo es hacer que entrenar sea más **claro, accesible, organizado y motivador** para cualquier persona.

---

## 📌 Índice
- [Descripción General](#descripción-general)
- [Características Principales](#características-principales)
- [Roles del Sistema](#roles-del-sistema)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Capturas del Sistema](#capturas-del-sistema)
  - [Landing Page](#landing-page)
  - [Login y Registro](#login-y-registro)
  - [Panel del Administrador](#panel-del-administrador)
  - [Panel del Cliente](#panel-del-cliente)
- [Flujo del Sistema](#flujo-del-sistema)
- [Próximas Funcionalidades](#próximas-funcionalidades)
- [Autor](#autor)

---

## 📖 Descripción General

FitPal nació con una idea simple:  
**hacer que entrenar sea más fácil, claro y motivador.**

La plataforma permite:

- Crear y asignar planes de entrenamiento personalizados  
- Gestionar sesiones y ejercicios  
- Registrar progreso diario  
- Mostrar métricas, logros y evolución del usuario  
- Ofrecer un panel para clientes y otro para administradores

Cada usuario recibe un plan acorde a su nivel, tiempo disponible y objetivo.

---

## ⭐ Características Principales

### ✔️ Para Clientes
- Ver planes de entrenamiento asignados  
- Ver sesiones del plan  
- Marcar ejercicios y sesiones como *pendientes* o *completadas*  
- Editar datos personales y preferencias  
- Registrar avances y progreso  
- (En desarrollo) Logros y estadísticas visuales  

### ✔️ Para Administradores
- Panel completo de gestión:  
  - CRUD de **planes**  
  - CRUD de **sesiones**  
  - CRUD de **ejercicios**  
  - CRUD de **usuarios**  
- Asignación de planes a usuarios  
- Vista centralizada del sistema  

---

## 👥 Roles del Sistema

### 🧑‍💼 Administrador
Credenciales por defecto:

Usuario: admin@fitness.com
Contraseña: admin123


Permisos:
- Crear, editar y eliminar planes  
- Crear, editar y eliminar sesiones  
- Crear, editar y eliminar ejercicios  
- Administrar usuarios  
- Acceder al panel administrativo completo  

---

### 🧑‍🦱 Cliente
Ejemplo de credenciales:

Usuario: maria.gonzalez@email.com
Contraseña: password123


Permisos:
- Ver planes asignados  
- Ver sesiones y ejercicios  
- Marcar progreso  
- Editar su perfil  

---

## 🛠️ Tecnologías Utilizadas

### **Frontend**
- React.js  
- HTML5  
- CSS3  
- Bootstrap  
- Fetch / Axios  

### **Backend**
- Python / Flask  
- Rutas REST  
- Control de autenticación  

### **Base de Datos**
- SQLite 
- Tablas:
  - usuarios
  - cliente 
  - plan_entrenamiento  
  - plan_sesion
  - sesion
  - sesion_ejercicio  
  - ejercicios  
  - progreso_usuario  
  - progreso_ejercicios  

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/irolon/FitPal
cd fitpal

### 2️⃣ Backend – Instalar dependencias
cd backend
pip install -r requirements.txt

### 3️⃣ Backend – Ejecutar Flask
python app.py

### 4️⃣ Frontend – Instalar dependencias
cd frontend
npm install

### 5️⃣ Frontend – Ejecutar React
npm run dev

### 6️⃣ Acceder a la app

Cliente: http://localhost:5173/
Backend: Cliente: http://localhost:5173/
Backend: http://localhost:5000/api/...

---

## 🏠 Landing Page

Incluye:
✔ ¿Qué es FitPal?
✔ Planes y beneficios
✔ Nuestras secciones
✔ Testimonios
✔ Nuestra Historia

## 🔐 Login y Registro

- Formulario moderno
- Inputs con iconos
- Estado de error
- Modo login / register

## 🧑‍💼 Panel del Administrador

El administrador cuenta con un panel central desde donde puede gestionar completamente el sistema FitPal.

### 📌 Dashboard Principal
El panel incluye accesos directos a:

- 📝 Planes  
- 📅 Sesiones  
- 🏋️ Ejercicios  
- 👥 Usuarios  
- ⚙️ Configuración (en desarrollo)

Permite navegar fácilmente por todas las herramientas de administración.

---

### 📌 Gestión de Planes
Aquí el administrador puede:

- Crear planes de entrenamiento
- Editar información existente
- Eliminar planes
- Buscar por nombre, frecuencia o cliente
- Visualizar la lista paginada de todos los planes
- Ver a qué cliente pertenece cada plan

Incluye tabla con:
- Nombre del plan  
- Frecuencia semanal  
- Cliente asignado  
- Acciones (Editar / Eliminar)

---

### 📌 Gestión de Sesiones
En esta sección se administran todas las sesiones disponibles.

Funciones:

- Crear sesiones nuevas
- Editar sesiones existentes
- Eliminar sesiones
- Ver descripción y estado
- Marcar como **Activa** o **Inactiva**
- Buscar por nombre o descripción

Columnas:
- Nombre  
- Descripción  
- Estado  
- Acciones  

---

### 📌 Gestión de Ejercicios
El administrador puede mantener actualizado el catálogo de ejercicios.

Permite:

- Crear ejercicios
- Editar ejercicios
- Eliminar ejercicios
- Buscar por nombre, categoría o descripción

Campos incluidos:
- Categoría (Calentamiento, Fuerza, etc.)
- Nombre del ejercicio
- Descripción
- Repeticiones
- Series
- Tiempo de descanso

---

### 📌 Gestión de Usuarios
Desde esta sección se administran todos los usuarios del sistema.

Opciones:

- Crear usuarios clientes o administradores
- Eliminar usuarios
- Buscar usuarios por nombre, apellido o correo

La tabla incluye:
- ID
- Nombre y apellido
- Correo
- Rol (administrador / cliente)
- Contraseña
- Acciones (Eliminar)

---

## 👤 Panel del Cliente

El cliente accede a un espacio personal donde puede ver y gestionar su entrenamiento asignado.

### 📌 Dashboard Personal
Incluye accesos a:

- **Mis Planes**
- **Sesiones**
- **Mi Progreso** (en desarrollo)
- **Logros** (en desarrollo)
- **Mi Perfil**

---

### 📌 Mis Planes
Aquí el usuario ve todos los planes que le fueron asignados.

La tabla muestra:

- Nombre del plan
- Frecuencia semanal
- Fecha de inicio
- Fecha de fin

Desde esta sección puede volver al dashboard personal.

---

### 📌 Mis Sesiones
El usuario puede visualizar sus sesiones del plan actual y registrar su progreso.

Incluye:

- Nombre de la sesión
- Descripción
- Progreso (Pendiente / Completado)
- Estado actual
- Botón **Ver Detalle**

El progreso de cada sesión se guarda en la base de datos.

---

### 📌 Ejercicios de la Sesión
Al entrar en "Ver Detalle", el usuario verá los ejercicios asignados a esa sesión.

La tabla incluye:

- Categoría  
- Nombre del ejercicio  
- Descripción  
- Repeticiones  
- Series  
- Descanso  
- Progreso (Pendiente / Completado)

Cada acción queda registrada en la base de datos.

---

### 📌 Mi Perfil
El cliente puede:

- Ver sus datos personales
- Modificar nombre, correo, DNI, fecha de inicio y edad
- Ver su plan actual y preferencias
- Acceder a sus sesiones desde el panel

Contiene tarjetas con:

- Información personal  
- Preferencias de entrenamiento  
- Sesiones activas y totales  

---


