import React, { useState } from 'react'
import { Link } from 'react-router-dom';


const CardTablaSesiones = ({ sesiones }) => {
  // Validar que sesiones sea un array
  const sesionesArray = Array.isArray(sesiones) ? sesiones : [];
  
  // Estado para manejar el estado de cada sesión individualmente
  const [estadosSesiones, setEstadosSesiones] = useState({});

  const handleEstadoChange = async (sesionId, nuevoEstado) => {
    try {
      const estadoBoolean = nuevoEstado === 'Completado';
      
      // Hacer la llamada HTTP para actualizar en la base de datos
      const response = await fetch(`http://localhost:5000/api/plan_sesion/sesion/${sesionId}/estado`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ estado: estadoBoolean })
      });

      if (response.ok) {
        // Solo actualizar el estado local si la llamada HTTP fue exitosa
        setEstadosSesiones(prev => ({
          ...prev,
          [sesionId]: nuevoEstado
        }));
        console.log(`Estado de sesión ${sesionId} actualizado a: ${nuevoEstado}`);
      } else {
        console.error('Error al actualizar el estado en la base de datos');
        alert('Error al actualizar el estado. Inténtalo de nuevo.');
      }
    } catch (error) {
      console.error('Error de conexión:', error);
      alert('Error de conexión. Verifica tu conexión a internet.');
    }
  }


  return (
    <div className="container vh-100 d-flex flex-column align-items-center justify-content-center">
          <h1 className="mb-4">Mis Sesiones de Entrenamiento</h1>
          <p>Aquí podrás ver y gestionar tus sesiones de entrenamiento asignadas.</p>

          <table className="table table-striped table-dark">
            <thead>
              <tr>
                <th>Nombre</th>
                <th>Descripcion</th>
                <th>Progreso</th>
                <th>Estado</th>
                <th>Detalle</th>
              </tr>
            </thead>
            <tbody>
              {sesionesArray.length === 0 ? (
                <tr>
                  <td colSpan="3" className="text-center">
                    No tenés sesiones de entrenamiento asignadas aún.
                  </td>
                </tr>
              ) : (
                sesionesArray.map((sesion) => (
                  <tr key={sesion.id}>
                    <td>{sesion.nombre}</td>
                    <td>{sesion.descripcion}</td>
                    <td>
                      <button 
                        className='btn btn-warning me-2' 
                        onClick={() => handleEstadoChange(sesion.id, 'Pendiente')}
                      >
                        Pendiente
                      </button>
                      <button 
                        className='btn btn-success' 
                        onClick={() => handleEstadoChange(sesion.id, 'Completado')}
                      >
                        Completado
                      </button>
                    </td>
                    <td>
                      <span className={`badge ${estadosSesiones[sesion.id] === 'Completado' ? 'bg-success' : estadosSesiones[sesion.id] === 'Pendiente' ? 'bg-warning' : 'bg-secondary'}`}>
                        {estadosSesiones[sesion.id] || (sesion.estado ? 'Completado' : 'Pendiente')}
                      </span>
                    </td>
                    <td>
                      <Link to={`/cliente/sesiones/${sesion.id}`} className="btn btn-info">Ver Detalle</Link>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
          <div>
            <a href="/cliente" className="btn btn-success mt-5">Volver a Mi Espacio</a>
          </div>
        </div>
  )
}

export default CardTablaSesiones