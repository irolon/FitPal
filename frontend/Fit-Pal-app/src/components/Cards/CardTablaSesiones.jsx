import React from 'react'

const CardTablaSesiones = ({ sesiones }) => {
  // Validar que sesiones sea un array
  const sesionesArray = Array.isArray(sesiones) ? sesiones : [];
  
  return (
    <div className="container vh-100 d-flex flex-column align-items-center justify-content-center">
          <h1 className="mb-4">Mis Sesiones de Entrenamiento</h1>
          <p>Aquí podrás ver y gestionar tus sesiones de entrenamiento asignadas.</p>

          <table className="table table-striped table-dark">
            <thead>
              <tr>
                <th>Nombre de la Sesión</th>
                <th>Fecha</th>
                <th>Estado</th>
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
                    <td>{sesion.fecha}</td>
                    <td>{sesion.estado}</td>
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