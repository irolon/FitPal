import { Link } from "react-router-dom";

const AdminHome = () => {
    const handleLogout = () => {
    localStorage.removeItem("user");
    navigate("/");
  };


  return (
    <div className="d-flex flex-column align-items-center justify-content-center min-vh-100">
      <div className="container">
        
        <div className="row mb-4">
          <div className="col text-center">
            <h1 className="section-title mb-3">Panel de administración</h1>
            <p className="section-subtitle">
              Gestioná usuarios, planes y ejercicios desde un solo lugar.
            </p>
          </div>
        </div>

      <div className="row g-4">



        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Planes</h5>
            <p className="flex-grow-1">
              Creá y editá planes de entrenamiento personalizados.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Gestionar planes</button>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Sesiones</h5>
            <p className="flex-grow-1">
              Creá o editá sesiones de entrenamiento para cargar en los Planes.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Gestionar sesiones</button>
            </div>
          </div>
        </div>

                <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Ejercicios</h5>
            <p className="flex-grow-1">
              Mantené actualizado el catálogo de ejercicios disponibles.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Gestionar Ejercicios</button>
            </div>
          </div>
        </div>

      </div>

      <div className="row g-4 mt-3 justify-content-center">

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Usuarios</h5>
            <p className="flex-grow-1">
              Administrá las cuentas de clientes y administradores.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Gestionar usuarios</button>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Configuración</h5>
            <p className="flex-grow-1">
              Accedé a ajustes generales del sistema y preferencias.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Configurar</button>
            </div>
          </div>
        </div>
        
        </div>


      </div>
              <div className="row mt-4">
                  <Link to="/" className="btn btn-danger mt-5" onClick={handleLogout}>Cerrar sesión</Link>
        </div>
    </div>
  );
};

export default AdminHome;
