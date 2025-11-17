import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

const CardEjercicios = ({ ejercicios, clienteId }) => {
  const [estadosEjercicios, setEstadosEjercicios] = useState({})
  const [loading, setLoading] = useState(false)

  // Cargar progreso al montar el componente
  useEffect(() => {
    const cargarProgreso = async () => {
      if (!clienteId) return
      
      try {
        const response = await fetch(`http://localhost:5000/api/progreso-ejercicio/cliente/${clienteId}`)
        if (response.ok) {
          const progreso = await response.json()
          setEstadosEjercicios(progreso)
        }
      } catch (error) {
        console.error('Error al cargar progreso:', error)
      }
    }

    cargarProgreso()
  }, [clienteId])

  // Función para actualizar el estado de un ejercicio
  const actualizarEstado = async (ejercicioId, nuevoEstado) => {
    if (!clienteId) {
      console.error('Cliente ID no disponible')
      return
    }

    setLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/progreso-ejercicio/actualizar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cliente_id: clienteId,
          ejercicio_id: ejercicioId,
          estado: nuevoEstado
        })
      })

      if (response.ok) {
        const resultado = await response.json()

        
        // Actualizar el estado local
        setEstadosEjercicios(prev => ({
          ...prev,
          [ejercicioId]: {
            estado: nuevoEstado,
            fecha_completado: nuevoEstado === 'completado' ? new Date().toISOString() : null
          }
        }))
      } else {
        const error = await response.json()
        alert('Error al actualizar el estado del ejercicio')
      }
    } catch (error) {
      alert('Error de conexión. Verifica que el servidor esté funcionando.')
    } finally {
      setLoading(false)
    }
  }

  // Función para obtener el estado actual de un ejercicio
  const obtenerEstado = (ejercicioId) => {
    const progreso = estadosEjercicios[ejercicioId]
    return progreso ? progreso.estado : 'pendiente'
  }

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
                                <button 
                                    className={`btn me-2 ${obtenerEstado(ejercicio.id) === 'pendiente' ? 'btn-warning' : 'btn-outline-warning'}`}
                                    onClick={() => actualizarEstado(ejercicio.id, 'pendiente')}
                                    disabled={loading}
                                >
                                    {loading ? '...' : 'Pendiente'}
                                </button>
                                <button 
                                    className={`btn ${obtenerEstado(ejercicio.id) === 'completado' ? 'btn-success' : 'btn-outline-success'}`}
                                    onClick={() => actualizarEstado(ejercicio.id, 'completado')}
                                    disabled={loading}
                                >
                                    {loading ? '...' : 'Completado'}
                                </button>
                            </td>
                            <td>
                                <span className={`badge ${obtenerEstado(ejercicio.id) === 'completado' ? 'bg-success' : obtenerEstado(ejercicio.id) === 'pendiente' ? 'bg-warning' : 'bg-secondary'}`}>
                                    {obtenerEstado(ejercicio.id) === 'completado' ? 'Completado' : 
                                     obtenerEstado(ejercicio.id) === 'pendiente' ? 'Pendiente' : 'Sin iniciar'}
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