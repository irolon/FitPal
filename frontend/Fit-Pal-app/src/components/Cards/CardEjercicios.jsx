import React from 'react'
import { Link } from 'react-router-dom'

const CardEjercicios = ({ ejercicios, clienteId }) => {
  return (
    <div className="container vh-100 d-flex flex-column align-items-center justify-content-center">
        <h1 className="mb-4">Ejercicios</h1>
        <p>Aquí podrás ver y gestionar tus ejercicios asignados.</p>

        <table className="table table-striped table-dark">
            <thead>
                <tr>
                    <th>Categoria</th>
                    <th>Nombre</th>
                    <th>Descripcion</th>
                    <th>Repeticiones</th>
                    <th>Series</th>
                    <th>Descanso</th>
                    <th>Progreso</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
                {ejercicios.length === 0 ? (
                    <tr>
                        <td colSpan="8" className="text-center">No hay ejercicios asignados.</td>
                    </tr>
                ) : (
                    ejercicios.map((ejercicio) => (
                        <tr key={ejercicio.id}>
                            <td>{ejercicio.categoria}</td>
                            <td>{ejercicio.nombre}</td>
                            <td>{ejercicio.descripcion}</td>
                            <td>{ejercicio.repeticiones}</td>
                            <td>{ejercicio.series}</td>
                            <td>{ejercicio.descanso}</td>
                            <td>
                                <button className='btn btn-warning me-2'>Pendiente</button>
                                <button className='btn btn-success'>Completado</button>
                            </td>
                            <td>
                                <span className={`badge ${ejercicio.estado === 'Completado' ? 'bg-success' : ejercicio.estado === 'Pendiente' ? 'bg-warning' : 'bg-secondary'}`}>
                                    {ejercicio.estado}
                                </span>
                            </td>
                        </tr>
                    ))
                )}
            </tbody>
        </table>
        <div>
            <Link to={`/cliente/${clienteId}/sesiones`} className="btn btn-success mt-5">Volver a Mi Espacio</Link>
        </div>   
        





    </div>
  )
}

export default CardEjercicios