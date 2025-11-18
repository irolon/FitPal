import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";


const ClienteHome = () => {
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState('');

  const handleClick = () => {
    setErrorMessage('Funcionalidad en desarrollo. Pronto estará disponible.');
  };
  
  // Obtener únicamente el user_id del localStorage
  const getUserIdFromStorage = () => {
    try {
      const userData = localStorage.getItem("user");
      if (userData) {
        try {
          const parsedData = JSON.parse(userData);
          return parsedData.user_id || '';
        } catch {
          const match = userData.match(/user_id:(\d+)/);
          return match ? match[1] : '';
        }
      }
      return '';
    } catch (error) {
      console.error("Error al obtener user ID:", error);
      return '';
    }
  };
  
  const user_id = getUserIdFromStorage();
  
  // Obtener el nombre del usuario del localStorage
  const getUserNameFromStorage = () => {
    try {
      const userData = localStorage.getItem("user");
      if (userData) {
        try {
          const parsedData = JSON.parse(userData);
          return parsedData.nombre || '';
        } catch {
          // Si no es JSON válido, buscar nombre en el string
          const match = userData.match(/nombre:([^,]+)/);
          return match ? match[1] : '';
        }
      }
      return '';
    } catch (error) {
      console.error("Error al obtener nombre del usuario:", error);
      return '';
    }
  };
  
  const userName = getUserNameFromStorage(); 
  const handleLogout = () => {
    localStorage.removeItem("user");
    navigate("/");
  };

  return (
    <div className="d-flex flex-column align-items-center justify-content-center div-home min-vh-100">
      <div className="container">

        <div className="row mb-4">
        <div className="col text-center">
          <h1 className="section-title mb-3">Hola {userName} !</h1>
          <p className="section-subtitle">
            Accedé a tus planes, sesiones, progreso y logros personales.
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
            <h5>Mis Planes</h5>
            <p className="flex-grow-1 mt-2">
              Consultá tus planes de entrenamiento personalizados según tu nivel y objetivos.
            </p>
            <div className="card-button-center">
              <Link to={`/cliente/${user_id}/planes`} className="btn btn-dark btn-lg mt-3">Ver planes</Link>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Sesiones</h5>
            <p className="flex-grow-1 mt-2">
              Revisá tus sesiones asignadas para cada día y marcá las que ya completaste.
            </p>
            <div className="card-button-center">
              <Link to={`/cliente/${user_id}/sesiones`} className="btn btn-dark btn-lg mt-3">Ver sesiones</Link>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Mi Progreso</h5>
            <p className="flex-grow-1 mt-2">
              Registrá tus entrenamientos y visualizá tu evolución mediante métricas y gráficos.
            </p>
            <div className="card-button-center">
              <Link onClick={handleClick} className="btn btn-dark btn-lg mt-3">Ver progreso</Link>
            </div>
          </div>
        </div>

      </div>

      <div className="row g-4 mt-3 justify-content-center">

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Logros</h5>
            <p className="flex-grow-1 mt-2">
              Obtené recompensas y desbloqueá nuevos niveles según tu constancia.
            </p>
            <div className="card-button-center">
              <Link onClick={handleClick} className="btn btn-dark btn-lg mt-3">Ver logros</Link>
            </div>
          </div>
        </div>

        <div className="col-12 col-md-4">
          <div className="card-fitpal h-100 d-flex flex-column">
            <h5>Mi Perfil</h5>
            <p className="flex-grow-1 mt-2">
              Editá tus datos personales, objetivos y preferencias de entrenamiento.
            </p>
            <div className="card-button-center">
              <Link onClick={handleClick} className="btn btn-dark btn-lg mt-3">Editar perfil</Link>
            </div>
          </div>
        </div>

        </div>

      </div>
      <div>
        <button className="btn btn-danger btn-lg mt-5" onClick={handleLogout} >Cerrar Sesión</button>
      </div>
    </div>
  );
};

export default ClienteHome;
