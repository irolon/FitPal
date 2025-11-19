import './App.css'
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import img_nos from './assets/img/img-6.jpg'
import img_plan from './assets/img/img-7.jpg'
import img_nov from './assets/img/img-8.jpg'

import NavBar from './components/NavBar/NavBar.jsx'
import HomeListContainer from './components/Inicio/HomeListContainer.jsx'
import Footer from './components/Footer/Footer.jsx'
import ContainerNosotros from './components/Rutas/ContainerNosotros.jsx'
import ContainerPlan from './components/Rutas/ContainerPlan.jsx'
import ContainerNovedades from './components/Rutas/ContainerNovedades.jsx'
import Login from './components/Login/Login.jsx'
import AdminHome from "./components/Home/AdminHome.jsx";
import ClienteHome from "./components/Home/ClienteHome.jsx";
import { ProtectedUserRoute, ProtectedAdminRoute } from './components/ProtectedRoute/ProtectedRoute.jsx'
import Planes from './components/Rutas/Planes.jsx'
import Sesiones from './components/Rutas/Sesiones.jsx'
import Ejercicios from './components/Rutas/Ejercicios.jsx'
import AdminEjercicios from './components/Rutas/AdminEjercicios.jsx'
import CrearEjercicio from "./components/Rutas/CrearEjercicio.jsx";
import EditarEjercicio from "./components/Rutas/EditarEjercicio.jsx";
import AdminSesiones from "./components/Rutas/AdminSesiones.jsx";
import AdminSesionEditar from "./components/Rutas/AdminSesionEditar.jsx";
import AdminSesionCrearWrapper from "./components/Rutas/AdminSesionCrear.jsx";
import AdminPlanes from "./components/Rutas/CardAdminPlanes.jsx";
import AdminPlanCrearWrapper from "./components/Rutas/AdminPlanesCrear.jsx";
import AdminPlanesEditar from "./components/Rutas/AdminPlanesEditar.jsx";
import PerfilCliente from "./components/Cliente/PerfilCliente.jsx";
import AdminUsuarios from "./components/Rutas/AdminUsuarios.jsx";

const API = import.meta.env.VITE_API_URL;

function AppContent() {
  const location = useLocation();
  const hideNavbar =
    location.pathname === '/admin' ||
    location.pathname === '/cliente' ||
    (location.pathname.startsWith('/cliente/') &&
      (location.pathname.includes('/planes') ||
        location.pathname.includes('/sesiones') ||
        location.pathname.includes('/ejercicios') ||
        location.pathname.includes('/perfil'))) ||
    (location.pathname.startsWith('/admin/') &&
      location.pathname.includes('/usuarios')) ||
    (location.pathname.startsWith('/admin/') &&
      location.pathname.includes('/ejercicios')) ||
    (location.pathname.startsWith('/admin/') &&
      location.pathname.includes('/sesiones'))||
    (location.pathname.startsWith('/admin/') &&
      location.pathname.includes('/planes'));

  return (
    <div className="d-flex flex-column min-vh-100">
      {!hideNavbar && <NavBar />}

      <Routes>
        <Route path='/' element={<HomeListContainer />} />
        <Route path='/nosotros' element={<ContainerNosotros titulo="Nuestra Historia" imagen={img_nos} />} />
        <Route path='/planes' element={<ContainerPlan titulo="Planes de Entrenamiento" imagen={img_plan} />} />
        <Route path='/novedades' element={<ContainerNovedades titulo="Novedades" imagen={img_nov} />} />
        <Route path='/login' element={<Login />} />

        <Route path='/admin' element={<ProtectedAdminRoute><AdminHome /></ProtectedAdminRoute>} />
        <Route path="/cliente" element={<ProtectedUserRoute><ClienteHome /></ProtectedUserRoute>} />

        <Route path='/cliente/:id/planes' element={<ProtectedUserRoute><Planes /></ProtectedUserRoute>} />
        <Route path='/cliente/:id/sesiones' element={<ProtectedUserRoute><Sesiones /></ProtectedUserRoute>} />
        <Route path='/cliente/:id/sesiones/ejercicios' element={<ProtectedUserRoute><Ejercicios /></ProtectedUserRoute>} />
        <Route path='/cliente/:id/perfil' element={<ProtectedUserRoute><PerfilCliente /></ProtectedUserRoute>} />

        <Route path='/admin/ejercicios' element={<ProtectedAdminRoute><AdminEjercicios /></ProtectedAdminRoute>} />
        <Route path='/admin/sesiones' element={<ProtectedAdminRoute><AdminSesiones /></ProtectedAdminRoute>} />
        <Route path='/admin/planes' element={<ProtectedAdminRoute><AdminPlanes /></ProtectedAdminRoute>} />
        <Route path='/admin/usuarios' element={<ProtectedAdminRoute><AdminUsuarios /></ProtectedAdminRoute>} />

        <Route path="/admin/planes/:id/editar" element={<ProtectedAdminRoute><AdminPlanesEditar /></ProtectedAdminRoute>} />
        <Route path="/admin/planes/crear" element={<ProtectedAdminRoute><AdminPlanCrearWrapper /></ProtectedAdminRoute>} />    

        <Route path="/admin/sesiones/:id/editar" element={<ProtectedAdminRoute><AdminSesionEditar /></ProtectedAdminRoute>} />
        <Route path="/admin/sesiones/crear" element={<ProtectedAdminRoute><AdminSesionCrearWrapper /></ProtectedAdminRoute>} />

        <Route path="/admin/ejercicios/crear" element={<ProtectedAdminRoute><CrearEjercicio /></ProtectedAdminRoute>} />
        <Route path="/admin/ejercicios/:id/editar" element={<ProtectedAdminRoute><EditarEjercicio /></ProtectedAdminRoute>} />

      </Routes>

      {!hideNavbar && <Footer />}
    </div>
  )
}

function App() {
  return (
    <BrowserRouter>
      <AppContent />
    </BrowserRouter>
  )
}

export default App
