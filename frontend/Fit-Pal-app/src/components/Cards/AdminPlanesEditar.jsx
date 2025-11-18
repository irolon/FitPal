import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";

const AdminPlanEditar = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [plan, setPlan] = useState({ nombre: "", frecuencia: "", fecha_inicio: "", fecha_fin: "", cliente_id: "", administrador_id: "" });
  const [sesiones, setSesiones] = useState([]);
  const [sesionesDisponibles, setSesionesDisponibles] = useState([]);
  const [mostrarModal, setMostrarModal] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:5000/api/admin/planes/${id}`)
      .then(res => res.json())
      .then(data =>
        setPlan({ 
          nombre: data.nombre, 
          frecuencia: data.frecuencia,
          fecha_inicio: data.fecha_inicio || "",
          fecha_fin: data.fecha_fin || "",
          cliente_id: data.cliente_id,
          administrador_id: data.administrador_id
        })
      )
      .catch(console.error);

    // Cargar sesiones del plan
    fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones`)
      .then(res => res.json())
      .then(data => setSesiones(data))
      .catch(console.error);
  }, [id]);

  const cargarSesionesDisponibles = () => {
    fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones/disponibles`)
      .then(res => res.json())
      .then(data => {
        // Asegurar que data sea un array
        if (Array.isArray(data)) {
          setSesionesDisponibles(data);
        } else {
          console.error('Datos de sesiones no válidos:', data);
          setSesionesDisponibles([]);
        }
      })
      .catch(error => {
        console.error('Error al cargar sesiones disponibles:', error);
        setSesionesDisponibles([]);
      });
  };

  const handleGuardar = (e) => {
    e.preventDefault();

    fetch(`http://localhost:5000/api/admin/planes/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(plan),
    })
      .then(res => res.json())
      .then(() => navigate("/admin/planes"))
      .catch(console.error);
  };

  const handleEliminarSesion = async (sesionId) => {
    const confirmar = window.confirm("¿Estás seguro de que quieres eliminar esta sesión del plan?");
    
    if (!confirmar) return;

    try {
      const response = await fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones/${sesionId}`, {
        method: "DELETE"
      });

      if (response.ok) {
        // Actualizar lista de sesiones
        setSesiones(sesiones.filter(s => s.sesion_id !== sesionId));
        alert("Sesión eliminada del plan exitosamente");
      } else {
        alert("Error al eliminar la sesión del plan");
      }
    } catch (error) {
      console.error("Error al eliminar sesión:", error);
      alert("Error al eliminar la sesión del plan");
    }
  };

  const handleAbrirModal = () => {
    cargarSesionesDisponibles();
    setMostrarModal(true);
  };

  const handleCerrarModal = () => {
    setMostrarModal(false);
    setSesionesDisponibles([]);
  };

  const handleAgregarSesion = async (sesionId) => {
    try {
      const response = await fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones/${sesionId}`, {
        method: "POST"
      });

      if (response.ok) {
        // Recargar sesiones del plan
        fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones`)
          .then(res => res.json())
          .then(data => setSesiones(data))
          .catch(console.error);
        
        handleCerrarModal();
        alert("Sesión agregada al plan exitosamente");
      } else {
        alert("Error al agregar la sesión al plan");
      }
    } catch (error) {
      console.error("Error al agregar sesión:", error);
      alert("Error al agregar la sesión al plan");
    }
  };



  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-4 text-center">Editar Plan</h1>

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
    </div>
  );
};

export default AdminPlanEditar;
