import React from 'react'
import { Link } from 'react-router-dom';

const CardTablaPlanes = ({ planes }) => {
  // Validar que planes sea un array
  const planesArray = Array.isArray(planes) ? planes : [];

  return (
    <div className=" vh-100 d-flex flex-column align-items-center div-home justify-content-center">
      <h1 className="mb-4">Mis Planes de Entrenamiento</h1>
      <p>Aquí podrás ver y gestionar tus planes de entrenamiento personalizados.</p>

      <table className="container table table-striped table-dark">
        <thead>
          <tr>
            <th>Nombre del Plan</th>
            <th>Frecuencia</th>
            <th>Fecha Inicio</th>
            <th>Fecha Fin</th>
          </tr>
        </thead>
        <tbody>
          {planesArray.length === 0 ? (
            <tr>
              <td colSpan="4" className="text-center">
                No tenés planes de entrenamiento cargados aún.
              </td>
            </tr>
          ) : (
            planesArray.map((plan) => (
              <tr key={plan.id}>
                <td>{plan.nombre}</td>
                <td>{plan.frecuencia}</td>
                <td>{plan.fecha_inicio}</td>
                <td>{plan.fecha_fin}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
      <div>
        <Link to="/cliente" className="btn btn-success mt-5">Volver a Mi Espacio</Link>
      </div>

    </div>
  )
}

export default CardTablaPlanes