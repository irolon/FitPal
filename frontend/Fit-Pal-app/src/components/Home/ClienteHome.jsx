const ClienteHome = () => {
  return (
    <div className="container my-5">

      <div className="row mb-4">
        <div className="col text-center">
          <h1 className="section-title mb-3">Mi espacio FitPal</h1>
          <p className="section-subtitle">
            Accedé a tus planes, sesiones, progreso y logros personales.
          </p>
        </div>
      </div>

      <div className="row g-4">

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Mis Planes</h5>
            <p className="flex-grow-1">
              Consultá tus planes de entrenamiento personalizados según tu nivel y objetivos.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Ver planes</button>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Sesiones</h5>
            <p className="flex-grow-1">
              Revisá tus sesiones asignadas para cada día y marcá las que ya completaste.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Ver sesiones</button>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Mi Progreso</h5>
            <p className="flex-grow-1">
              Registrá tus entrenamientos y visualizá tu evolución mediante métricas y gráficos.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Ver progreso</button>
            </div>
          </div>
        </div>

      </div>

      <div className="row g-4 mt-3 justify-content-center">

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Logros</h5>
            <p className="flex-grow-1">
              Obtené recompensas y desbloqueá nuevos niveles según tu constancia.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Ver logros</button>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Mi Perfil</h5>
            <p className="flex-grow-1">
              Editá tus datos personales, objetivos y preferencias de entrenamiento.
            </p>
            <div className="card-button-center">
              <button className="btn-fitpal">Editar perfil</button>
            </div>
          </div>
        </div>

      </div>

    </div>
  );
};

export default ClienteHome;
