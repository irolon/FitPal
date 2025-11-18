import { Link } from "react-router-dom";
import { useState } from "react";


  const AdminHome = () => {
    const [errorMessage, setErrorMessage] = useState('');


    const handleLogout = () => {
      localStorage.removeItem("user");
      navigate("/");
    };
    const handleClick = () => {
    setErrorMessage('Funcionalidad en desarrollo. Pronto estará disponible.');
  };


  return (
    <div className="d-flex flex-column align-items-center justify-content-center min-vh-100 div-home">
      <div className="container">
        
        <div className="row mb-4">
          <div className="col text-center">
            <h1 className="section-title mb-3">Panel de administración</h1>
            <p className="section-subtitle mt-2">
              Gestioná usuarios, planes y ejercicios desde un solo lugar.
            </p>
            {errorMessage && (
              <div className="alert alert-danger" role="alert">
                {errorMessage}
              </div>
            )}            
          </div>
          
        </div>

      <div className="row g-4">



        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Planes</h5>
            <p className="flex-grow-1 mt-2">
              Creá y editá planes de entrenamiento personalizados.
            </p>
            <div className="card-button-center">
                  <Link to="/admin/planes" className="btn btn-dark btn-lg mt-3">
                    Gestionar planes
                  </Link>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Sesiones</h5>
            <p className="flex-grow-1 mt-2">
              Creá o editá sesiones de entrenamiento para cargar en los Planes.
            </p>
            <div className="card-button-center">
                  <Link to="/admin/sesiones" className="btn btn-dark btn-lg mt-3">
                    Gestionar sesiones
                  </Link>
            </div>
          </div>
        </div>

                <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Ejercicios</h5>
            <p className="flex-grow-1 mt-2">
              Mantené actualizado el catálogo de ejercicios disponibles.
            </p>
            <div className="card-button-center">
                  <Link to="/admin/ejercicios" className="btn btn-dark btn-lg mt-3">
                    Gestionar ejercicios
                  </Link>
            </div>
          </div>
        </div>

      </div>

      <div className="row g-4 mt-3 justify-content-center">

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Usuarios</h5>
            <p className="flex-grow-1 mt-2">
              Administrá las cuentas de clientes y administradores.
            </p>
            <div className="card-button-center">
                  <Link to="/admin/usuarios" className="btn btn-dark btn-lg mt-3">
                    Gestionar usuarios
                  </Link>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Configuración</h5>
            <p className="flex-grow-1 mt-2">
              Accedé a ajustes generales del sistema y preferencias.
            </p>
            <div className="card-button-center">
                  <Link onClick={handleClick} className="btn btn-dark btn-lg mt-3">
                    Configuración
                  </Link>
            </div>
          </div>
        </div>
        
        </div>


      </div>
              <div className="row mt-4">
                  <Link to="/" className="btn btn-danger btn-lg mt-5" onClick={handleLogout} >Cerrar sesión</Link>
        </div>
    </div>
  );
};

export default AdminHome;
