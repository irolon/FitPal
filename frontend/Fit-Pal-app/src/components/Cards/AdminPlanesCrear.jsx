import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

const AdminPlanCrear = () => {
  const navigate = useNavigate();

  const [plan, setPlan] = useState({ nombre: "", descripcion: "" });
  const [sesionesDisponibles, setSesionesDisponibles] = useState([]);
  const [sesionesSeleccionadas, setSesionesSeleccionadas] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  useEffect(() => {
    fetch("http://localhost:5000/api/admin/sesiones")
      .then(res => res.json())
      .then(data => setSesionesDisponibles(data))
      .catch(console.error);
  }, []);

  const handleGuardar = (e) => {
    e.preventDefault();

    fetch("http://localhost:5000/api/admin/planes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(plan),
    })
      .then(res => res.json())
      .then(async (nuevoPlan) => {
        for (const ses of sesionesSeleccionadas) {
          await fetch(`http://localhost:5000/api/plan_sesion/${nuevoPlan.id}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sesion_id: ses.id }),
          });
        }
        navigate("/admin/planes");
      })
      .catch(console.error);
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
          <div className="mb-3">
            <label className="form-label">Nombre</label>
            <input
              type="text"
              className="form-control"
              value={plan.nombre}
              onChange={(e) => setPlan({ ...plan, nombre: e.target.value })}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Descripción</label>
            <textarea
              className="form-control"
              value={plan.descripcion}
              onChange={(e) => setPlan({ ...plan, descripcion: e.target.value })}
            />
          </div>
        </form>

        <div className="row">
          <div className="col-md-6">
            <h4>Sesiones Seleccionadas</h4>

            <ul className="list-group">
              {sesionesSeleccionadas.map(s => (
                <li key={s.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {s.nombre}
                  <button className="btn btn-sm btn-danger" onClick={() => quitarSesion(s.id)}>Quitar</button>
                </li>
              ))}

              {sesionesSeleccionadas.length === 0 &&
                <li className="list-group-item">No hay sesiones seleccionadas</li>}
            </ul>
          </div>

          <div className="col-md-6">
            <h4>Sesiones Disponibles</h4>

            <input
              type="text"
              className="form-control mb-2"
              placeholder="Buscar sesión..."
              value={searchTerm}
              onChange={(e) => {
                setSearchTerm(e.target.value);
                setCurrentPage(1);
              }}
            />

            <ul className="list-group">
              {currentItems.map(s => (
                <li key={s.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {s.nombre}
                  <button className="btn btn-sm btn-primary" onClick={() => agregarSesion(s)}>Agregar</button>
                </li>
              ))}

              {sesionesFiltradas.length === 0 &&
                <li className="list-group-item">No hay sesiones disponibles</li>}
            </ul>

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

        <div className="text-center mt-4 d-flex justify-content-center gap-3">
          <button onClick={handleGuardar} className="btn btn-success btn-lg">Crear Plan</button>
          <Link to="/admin/planes" className="btn btn-secondary btn-lg">Volver</Link>
        </div>
      </div>

    </div>
  );
};

export default AdminPlanCrear;
