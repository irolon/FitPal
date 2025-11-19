import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

const AdminPlanCrear = () => {
  const navigate = useNavigate();

  const [plan, setPlan] = useState({ 
    nombre: "", 
    frecuencia: "", 
    fecha_inicio: "", 
    fecha_fin: "", 
    cliente_id: "", 
    administrador_id: "1" 
  });
  const [clientes, setClientes] = useState([]);
  const [sesionesDisponibles, setSesionesDisponibles] = useState([]);
  const [sesionesSeleccionadas, setSesionesSeleccionadas] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  useEffect(() => {
    // Cargar sesiones
    fetch("http://localhost:5000/api/admin/sesiones")
      .then(res => res.json())
      .then(data => setSesionesDisponibles(data))
      .catch(console.error);
    
    // Cargar clientes
    fetch("http://localhost:5000/api/admin/clientes")
      .then(res => res.json())
      .then(data => setClientes(data))
      .catch(console.error);
  }, []);

  const handleGuardar = async (e) => {
    e.preventDefault();

    // Validar campos obligatorios
    if (!plan.nombre || !plan.frecuencia || !plan.cliente_id || !plan.fecha_inicio) {
      alert("Por favor, complete todos los campos obligatorios");
      return;
    }

    try {
      // Crear el plan
      const response = await fetch("http://localhost:5000/api/admin/planes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(plan),
      });
      
      const nuevoPlan = await response.json();
      
      if (response.ok && nuevoPlan.id) {
        // Agregar sesiones al plan
        for (let i = 0; i < sesionesSeleccionadas.length; i++) {
          const sesion = sesionesSeleccionadas[i];
          await fetch(`http://localhost:5000/api/admin/planes/${nuevoPlan.id}/sesiones/${sesion.id}`, {
            method: "POST"
          });
        }
        
        alert("Plan creado exitosamente");
        navigate("/admin/planes");
      } else {
        alert("Error al crear el plan: " + (nuevoPlan.error || "Error desconocido"));
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error al crear el plan");
    }
  };

  const agregarSesion = (s) => {
    setSesionesSeleccionadas([...sesionesSeleccionadas, s]);
  };

  const quitarSesion = (id) => {
    setSesionesSeleccionadas(sesionesSeleccionadas.filter(s => s.id !== id));
  };

  const sesionesFiltradas = sesionesDisponibles
    .filter(s => !sesionesSeleccionadas.some(sel => sel.id === s.id))
    .filter(s => s.nombre.toLowerCase().includes(searchTerm.toLowerCase()));

  const totalPages = Math.ceil(sesionesFiltradas.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const currentItems = sesionesFiltradas.slice(startIndex, startIndex + itemsPerPage);

  const cambiarPagina = (p) => {
    if (p >= 1 && p <= totalPages) {
      setCurrentPage(p);
    }
  };

  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-4 text-center">Crear Plan</h1>

      <div className="container">
        <form onSubmit={handleGuardar} className="container mb-4">
          <div className="row">
            <div className="col-md-6">
              <div className="mb-3">
                <label className="form-label">Nombre del Plan *</label>
                <input
                  type="text"
                  className="form-control"
                  value={plan.nombre}
                  onChange={(e) => setPlan({ ...plan, nombre: e.target.value })}
                  required
                  placeholder="Ej: Plan de Fuerza Inicial"
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Frecuencia (días por semana) *</label>
                <select
                  className="form-control"
                  value={plan.frecuencia}
                  onChange={(e) => setPlan({ ...plan, frecuencia: e.target.value })}
                  required
                >
                  <option value="">Seleccionar frecuencia...</option>
                  <option value="1">1 día por semana</option>
                  <option value="2">2 días por semana</option>
                  <option value="3">3 días por semana</option>
                  <option value="4">4 días por semana</option>
                  <option value="5">5 días por semana</option>
                  <option value="6">6 días por semana</option>
                  <option value="7">7 días por semana</option>
                </select>
              </div>

              <div className="mb-3">
                <label className="form-label">Cliente *</label>
                <select
                  className="form-control"
                  value={plan.cliente_id}
                  onChange={(e) => setPlan({ ...plan, cliente_id: e.target.value })}
                  required
                >
                  <option value="">Seleccionar cliente...</option>
                  {clientes.map(cliente => (
                    <option key={cliente.id} value={cliente.id}>
                      {cliente.nombre} {cliente.apellido}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <div className="col-md-6">
              <div className="mb-3">
                <label className="form-label">Fecha de Inicio *</label>
                <input
                  type="date"
                  className="form-control"
                  value={plan.fecha_inicio}
                  onChange={(e) => setPlan({ ...plan, fecha_inicio: e.target.value })}
                  required
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Fecha de Fin</label>
                <input
                  type="date"
                  className="form-control"
                  value={plan.fecha_fin}
                  onChange={(e) => setPlan({ ...plan, fecha_fin: e.target.value })}
                  min={plan.fecha_inicio}
                />
                <div className="form-text">Opcional. Si no se especifica, el plan no tendrá fecha límite.</div>
              </div>
            </div>
          </div>

          <hr className="my-4" />
        </form>

        <h3 className="mb-3">Asignar Sesiones al Plan</h3>
        <div className="row">
          <div className="col-md-6">
            <h5>Sesiones Seleccionadas ({sesionesSeleccionadas.length})</h5>

            <div className="border rounded p-3" style={{minHeight: '300px', maxHeight: '400px', overflowY: 'auto'}}>
              {sesionesSeleccionadas.length === 0 ? (
                <div className="text-center text-muted py-4">
                  <i className="bi bi-plus-circle" style={{fontSize: '3rem'}}></i>
                  <p>No hay sesiones seleccionadas</p>
                  <small>Selecciona sesiones de la lista de la derecha</small>
                </div>
              ) : (
                <div className="list-group list-group-flush">
                  {sesionesSeleccionadas.map((s, index) => (
                    <div key={s.id} className="list-group-item d-flex justify-content-between align-items-start px-0">
                      <div>
                        <h6 className="mb-1">{s.nombre}</h6>
                        <small className="text-muted">Posición: {index + 1}</small>
                        {s.descripcion && <p className="mb-1 small">{s.descripcion}</p>}
                      </div>
                      <button 
                        className="btn btn-sm btn-outline-danger" 
                        onClick={() => quitarSesion(s.id)}
                        title="Quitar sesión"
                      >
                        <i className="bi bi-x"></i>
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          <div className="col-md-6">
            <h5>Sesiones Disponibles</h5>

            <div className="mb-3">
              <input
                type="text"
                className="form-control"
                placeholder=" Buscar sesión..."
                value={searchTerm}
                onChange={(e) => {
                  setSearchTerm(e.target.value);
                  setCurrentPage(1);
                }}
              />
            </div>

            <div className="border rounded p-2" style={{height: '300px', overflowY: 'auto'}}>
              {sesionesFiltradas.length === 0 ? (
                <div className="text-center text-muted py-4">
                  <i className="bi bi-search" style={{fontSize: '2rem'}}></i>
                  <p>No hay sesiones disponibles</p>
                  {searchTerm && <small>Prueba con otros términos de búsqueda</small>}
                </div>
              ) : (
                <div className="list-group list-group-flush">
                  {currentItems.map(s => (
                    <div key={s.id} className="list-group-item d-flex justify-content-between align-items-start px-2">
                      <div className="flex-grow-1">
                        <h6 className="mb-1">{s.nombre}</h6>
                        {s.descripcion && <small className="text-muted">{s.descripcion}</small>}
                      </div>
                      <button 
                        className="btn btn-sm btn-outline-primary ms-2" 
                        onClick={() => agregarSesion(s)}
                        title="Agregar sesión"
                      >
                        <i className="bi bi-plus"></i>
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {totalPages > 1 && (
              <div className="d-flex justify-content-center mt-3">
                <button
                  className="btn btn-secondary mx-1"
                  onClick={() => cambiarPagina(currentPage - 1)}
                  disabled={currentPage === 1}
                >
                  Anterior
                </button>

                <span className="mx-2">Página {currentPage} de {totalPages}</span>

                <button
                  className="btn btn-secondary mx-1"
                  onClick={() => cambiarPagina(currentPage + 1)}
                  disabled={currentPage === totalPages}
                >
                  Siguiente
                </button>
              </div>
            )}
          </div>
        </div>

        <hr className="my-4" />
        
        {/* Resumen del plan antes de crear */}
        {plan.nombre && plan.cliente_id && plan.frecuencia && plan.fecha_inicio && (
          <div className="alert alert-info">
            <h6><i className="bi bi-info-circle"></i> Resumen del Plan</h6>
            <div className="row">
              <div className="col-md-6">
                <strong>Nombre:</strong> {plan.nombre}<br/>
                <strong>Frecuencia:</strong> {plan.frecuencia} día(s) por semana<br/>
                <strong>Fecha de inicio:</strong> {new Date(plan.fecha_inicio).toLocaleDateString()}
              </div>
              <div className="col-md-6">
                <strong>Cliente:</strong> {clientes.find(c => c.id == plan.cliente_id)?.nombre} {clientes.find(c => c.id == plan.cliente_id)?.apellido}<br/>
                {plan.fecha_fin && <><strong>Fecha de fin:</strong> {new Date(plan.fecha_fin).toLocaleDateString()}<br/></>}
                <strong>Sesiones:</strong> {sesionesSeleccionadas.length} seleccionada(s)
              </div>
            </div>
          </div>
        )}

        <div className="text-center mt-4 d-flex justify-content-center gap-3">
          <button 
            onClick={handleGuardar} 
            className="btn btn-success btn-lg"
            disabled={!plan.nombre || !plan.cliente_id || !plan.frecuencia || !plan.fecha_inicio}
          >
           Crear Plan
          </button>
          <Link to="/admin/planes" className="btn btn-secondary btn-lg">
            Cancelar
          </Link>
        </div>
      </div>

    </div>
  );
};

export default AdminPlanCrear;
