import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom';


const CardTablaSesiones = ({ sesiones, clienteId }) => {
  // Validar que sesiones sea un array
  const sesionesArray = Array.isArray(sesiones) ? sesiones : [];
  
  // Estado para manejar el estado de cada sesión individualmente
  const [estadosSesiones, setEstadosSesiones] = useState({});

  // Inicializar el estado con los datos de la BD cuando cambian las sesiones
  useEffect(() => {
    if (sesionesArray.length > 0) {
      const estadosIniciales = {};
      sesionesArray.forEach(sesion => {
        estadosIniciales[sesion.id] = sesion.estado ? 'Completado' : 'Pendiente';
      });
      setEstadosSesiones(estadosIniciales);
    }
  }, [sesionesArray]);

  const handleEstadoChange = async (sesionId, nuevoEstado) => {
    try {
      
      // Validar que clienteId existe
      if (!clienteId) {
        console.error('clienteId no está definido');
        alert('Error: No se pudo identificar el cliente');
        return;
      }

      const estadoBoolean = nuevoEstado === 'Completado';
      
      // Hacer la llamada HTTP para actualizar en la base de datos
      const response = await fetch(`http://localhost:5000/api/plan_sesion/cliente/${clienteId}/sesion/${sesionId}/estado`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ estado: estadoBoolean })
      });

      if (response.ok) {
        // Solo actualizar el estado local si la llamada HTTP esta okk
        setEstadosSesiones(prev => ({
          ...prev,
          [sesionId]: nuevoEstado
        }));
      } else {
        const errorText = await response.text();
        console.error('Error al actualizar el estado:', response.status, errorText);
        alert(`Error al actualizar el estado (${response.status}). Inténtalo de nuevo.`);
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
                  <td colSpan="5" className="text-center">
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
                        {estadosSesiones[sesion.id]}
                      </span>
                    </td>
                    <td>
                      <Link to={`/cliente/${clienteId}/sesiones/ejercicios`} className="btn btn-info">Ver Detalle</Link>
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