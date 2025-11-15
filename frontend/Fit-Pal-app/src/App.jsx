import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import{BrowserRouter,Routes,Route} from 'react-router-dom'
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


const API = import.meta.env.VITE_API_URL;

function App() {


  
  return (
    <div className="d-flex flex-column min-vh-100">   
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route path='/' element={<HomeListContainer/>}/>
          <Route path='/nosotros' element={<ContainerNosotros titulo="Nuestra Historia" imagen={img_nos}/>}/>
          <Route path='/planes' element={<ContainerPlan titulo="Planes de Entrenamiento" imagen={img_plan}/>}/>
          <Route path='/novedades' element={<ContainerNovedades titulo="Novedades" imagen={img_nov}/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/admin' element={<AdminHome/>}/>
          <Route path="/cliente" element={<ClienteHome />} />
        </Routes>
        <Footer/>
      </BrowserRouter>
    </div>
  )
}

export default App
