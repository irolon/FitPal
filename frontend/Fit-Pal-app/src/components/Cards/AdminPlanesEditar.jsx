import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";

const AdminPlanEditar = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [plan, setPlan] = useState({ nombre: "", descripcion: "" });
  const [ejerciciosPlan, setEjerciciosPlan] = useState([]);
  const [ejerciciosDisponibles, setEjerciciosDisponibles] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  useEffect(() => {
    fetch(`http://localhost:5000/api/admin/planes/${id}`)
      .then(res => res.json())
      .then(data =>
        setPlan({ nombre: data.nombre, descripcion: data.descripcion })
      )
      .catch(console.error);

    fetch(`http://localhost:5000/api/plan_ejercicio/${id}`)
      .then(res => res.json())
      .then(data => setEjerciciosPlan(data))
      .catch(console.error);

    fetch("http://localhost:5000/api/admin/ejercicios")
      .then(res => res.json())
      .then(data => setEjerciciosDisponibles(data))
      .catch(console.error);
  }, [id]);

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

  const agregarEjercicio = (ejId) => {
    fetch(`http://localhost:5000/api/plan_ejercicio/${id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ejercicio_id: ejId }),
    })
      .then(() => {
        const ej = ejerciciosDisponibles.find(e => e.id === ejId);
        setEjerciciosPlan([...ejerciciosPlan, ej]);
      })
      .catch(console.error);
  };

  const quitarEjercicio = (ejId) => {
    fetch(`http://localhost:5000/api/plan_ejercicio/${id}/${ejId}`, {
      method: "DELETE"
    })
      .then(() => {
        setEjerciciosPlan(ejerciciosPlan.filter(e => e.id !== ejId));
      })
      .catch(console.error);
  };

  const ejerciciosFiltrados = ejerciciosDisponibles
    .filter(e => !ejerciciosPlan.some(ep => ep.id === e.id))
    .filter(e => e.nombre.toLowerCase().includes(searchTerm.toLowerCase()));

  const totalPages = Math.ceil(ejerciciosFiltrados.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const currentItems = ejerciciosFiltrados.slice(startIndex, startIndex + itemsPerPage);

  const cambiarPagina = (p) => {
    if (p >= 1 && p <= totalPages) setCurrentPage(p);
  };

  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-4 text-center">Editar Plan</h1>

      <div className="container">
        <form onSubmit={handleGuardar} className="mb-4">
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
            <h4>Ejercicios del Plan</h4>
            <ul className="list-group">
              {ejerciciosPlan.map(e => (
                <li key={e.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {e.nombre}
                  <button className="btn btn-sm btn-danger" onClick={() => quitarEjercicio(e.id)}>
                    Quitar
                  </button>
                </li>
              ))}
              {ejerciciosPlan.length === 0 &&
                <li className="list-group-item">No hay ejercicios asignados</li>}
            </ul>
          </div>

          <div className="col-md-6">
            <h4>Ejercicios Disponibles</h4>

            <input
              type="text"
              className="form-control mb-2"
              placeholder="Buscar ejercicio..."
              value={searchTerm}
              onChange={(e) => {
                setSearchTerm(e.target.value);
                setCurrentPage(1);
              }}
            />

            <ul className="list-group">
              {currentItems.map(e => (
                <li key={e.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {e.nombre}
                  <button className="btn btn-sm btn-primary" onClick={() => agregarEjercicio(e.id)}>
                    Agregar
                  </button>
                </li>
              ))}

              {ejerciciosFiltrados.length === 0 &&
                <li className="list-group-item">No hay ejercicios disponibles</li>}
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
          <button onClick={handleGuardar} className="btn btn-success btn-lg">
            Guardar Cambios
          </button>
          <Link to="/admin/planes" className="btn btn-secondary btn-lg">
            Volver
          </Link>
        </div>
      </div>
    </div>
  );
};

export default AdminPlanEditar;
