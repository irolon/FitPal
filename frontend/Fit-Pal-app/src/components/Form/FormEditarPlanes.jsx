import React from 'react'
import { Link } from 'react-router-dom'

const FormEditarPlanes = ({ plan, setPlan, handleGuardar, sesiones, handleAbrirModal,
     handleEliminarSesion, mostrarModal, handleCerrarModal, sesionesDisponibles, handleAgregarSesion }) => {
        
  return (
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <form onSubmit={handleGuardar}>
              <div className="mb-3">
                <label className="form-label">Nombre del Plan</label>
                <input
                  type="text"
                  className="form-control"
                  value={plan.nombre}
                  onChange={(e) => setPlan({ ...plan, nombre: e.target.value })}
                  required
                  placeholder="Ingrese el nombre del plan"
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Frecuencia Semanal (1-7 días)</label>
                <select
                  className="form-control"
                  value={plan.frecuencia}
                  onChange={(e) => setPlan({ ...plan, frecuencia: e.target.value })}
                  required
                >
                  <option value="">Seleccione la frecuencia</option>
                  <option value="1">1 vez por semana</option>
                  <option value="2">2 veces por semana</option>
                  <option value="3">3 veces por semana</option>
                  <option value="4">4 veces por semana</option>
                  <option value="5">5 veces por semana</option>
                  <option value="6">6 veces por semana</option>
                  <option value="7">7 veces por semana (diario)</option>
                </select>
              </div>

              <div className="mb-3">
                <label className="form-label">Fecha de Inicio</label>
                <input
                  type="date"
                  className="form-control"
                  value={plan.fecha_inicio}
                  onChange={(e) => setPlan({ ...plan, fecha_inicio: e.target.value })}
                  required
                />
              </div>

              <div className="mb-4">
                <label className="form-label">Fecha de Fin</label>
                <input
                  type="date"
                  className="form-control"
                  value={plan.fecha_fin}
                  onChange={(e) => setPlan({ ...plan, fecha_fin: e.target.value })}
                  min={plan.fecha_inicio}
                />
              </div>

              <div className="d-flex justify-content-center gap-3 mb-4">
                <button type="submit" className="btn btn-success btn-lg">
                  Guardar Cambios
                </button>
                <Link to="/admin/planes" className="btn btn-secondary btn-lg">
                  Cancelar
                </Link>
              </div>
            </form>
          </div>
        </div>

        {/* Sección de Sesiones del Plan */}
        <div className="row justify-content-center mt-4">
          <div className="col-md-8">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h4 className="mb-0">Sesiones Asignadas al Plan</h4>
              <button 
                className="btn btn-success"
                onClick={handleAbrirModal}
              >
                Agregar Sesión
              </button>
            </div>
            
            {sesiones.length === 0 ? (
              <div className="alert alert-info text-center">
                <p className="mb-0">No hay sesiones asignadas a este plan</p>
              </div>
            ) : (
              <div className="card">
                <div className="card-body">
                  <div className="list-group">
                    {sesiones.map((sesion, index) => (
                      <div key={sesion.sesion_id} className="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                          <h6 className="mb-1">{sesion.nombre}</h6>
                          <p className="mb-1 text-muted">{sesion.descripcion}</p>
                          <small className="text-muted">Orden: {sesion.orden}</small>
                        </div>
                        <button 
                          className="btn btn-danger btn-sm"
                          onClick={() => handleEliminarSesion(sesion.sesion_id)}
                          title="Eliminar sesión del plan"
                        >
                          Quitar
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {mostrarModal && (
          <div className="modal show d-block" tabIndex="-1" style={{backgroundColor: 'rgba(0,0,0,0.5)'}}>
            <div className="modal-dialog modal-lg">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">Agregar Sesión al Plan</h5>
                  <button 
                    type="button" 
                    className="btn-close" 
                    onClick={handleCerrarModal}
                  ></button>
                </div>
                <div className="modal-body">
                  {!Array.isArray(sesionesDisponibles) || sesionesDisponibles.length === 0 ? (
                    <div className="alert alert-info text-center">
                      <p className="mb-0">No hay sesiones disponibles para agregar</p>
                    </div>
                  ) : (
                    <div className="list-group">
                      {sesionesDisponibles.map((sesion) => (
                        <div key={sesion.id} className="list-group-item d-flex justify-content-between align-items-center">
                          <div>
                            <h6 className="mb-1">{sesion.nombre}</h6>
                            <p className="mb-0 text-muted">{sesion.descripcion}</p>
                          </div>
                          <button 
                            className="btn btn-primary btn-sm"
                            onClick={() => handleAgregarSesion(sesion.id)}
                          >
                            Agregar
                          </button>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
                <div className="modal-footer">
                  <button 
                    type="button" 
                    className="btn btn-secondary" 
                    onClick={handleCerrarModal}
                  >
                    Cerrar
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}


      </div>
  )
}

export default FormEditarPlanes