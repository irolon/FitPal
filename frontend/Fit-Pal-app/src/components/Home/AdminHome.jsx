

const AdminHome = () => {
  return (
    <div className="d-flex align-items-center justify-content-center min-vh-100">
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
            <h5>Ejercicios</h5>
            <p className="flex-grow-1">
              Mantené actualizado el catálogo de ejercicios disponibles.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Gestionar ejercicios</button>
            </div>
          </div>
        </div>

      </div>

      <div className="row g-4 mt-3 justify-content-center">

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Reportes</h5>
            <p className="flex-grow-1">
              Visualizá métricas generales del sistema y progreso global.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Ver reportes</button>
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
    </div>
  );
};

export default AdminHome;
