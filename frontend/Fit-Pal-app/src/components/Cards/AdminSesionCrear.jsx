import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

const AdminSesionCrear = () => {
  const navigate = useNavigate();

  const [sesion, setSesion] = useState({ nombre: "", descripcion: "" });
  const [ejerciciosDisponibles, setEjerciciosDisponibles] = useState([]);
  const [ejerciciosSeleccionados, setEjerciciosSeleccionados] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  useEffect(() => {
    fetch("http://localhost:5000/api/admin/ejercicios")
      .then(res => res.json())
      .then(data => setEjerciciosDisponibles(data))
      .catch(console.error);
  }, []);

  const handleGuardar = (e) => {
    e.preventDefault();

    fetch("http://localhost:5000/api/admin/sesiones", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(sesion),
    })
      .then(res => res.json())
      .then(async (nuevaSesion) => {
        for (const ej of ejerciciosSeleccionados) {
          await fetch(`http://localhost:5000/api/sesion_ejercicio/${nuevaSesion.id}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ejercicio_id: ej.id }),
          });
        }
        navigate("/admin/sesiones");
      })
      .catch(console.error);
  };

  const agregarEjercicio = (ej) => {
    setEjerciciosSeleccionados([...ejerciciosSeleccionados, ej]);
  };

  const quitarEjercicio = (id) => {
    setEjerciciosSeleccionados(ejerciciosSeleccionados.filter(e => e.id !== id));
  };

  const ejerciciosFiltrados = ejerciciosDisponibles
    .filter(e => !ejerciciosSeleccionados.some(es => es.id === e.id))
    .filter(e => e.nombre.toLowerCase().includes(searchTerm.toLowerCase()));

  const totalPages = Math.ceil(ejerciciosFiltrados.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const currentItems = ejerciciosFiltrados.slice(startIndex, startIndex + itemsPerPage);

  const cambiarPagina = (p) => {
    if (p >= 1 && p <= totalPages) {
      setCurrentPage(p);
    }
  };

  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-4 text-center">Crear Sesión</h1>

      <div className="container">
        <form onSubmit={handleGuardar} className="container mb-4">
          <div className="mb-3">
            <label className="form-label">Nombre</label>
            <input
              type="text"
              className="form-control"
              value={sesion.nombre}
              onChange={(e) => setSesion({ ...sesion, nombre: e.target.value })}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Descripción</label>
            <textarea
              className="form-control"
              value={sesion.descripcion}
              onChange={(e) => setSesion({ ...sesion, descripcion: e.target.value })}
            />
          </div>

          <button type="submit" className="btn btn-success">Crear Sesión</button>
        </form>

        <div className="row">
          <div className="col-md-6">
            <h4>Ejercicios Seleccionados</h4>

            <ul className="list-group">
              {ejerciciosSeleccionados.map(e => (
                <li key={e.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {e.nombre}
                  <button className="btn btn-sm btn-danger" onClick={() => quitarEjercicio(e.id)}>Quitar</button>
                </li>
              ))}

              {ejerciciosSeleccionados.length === 0 &&
                <li className="list-group-item">No hay ejercicios seleccionados</li>}
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
                  <button className="btn btn-sm btn-primary" onClick={() => agregarEjercicio(e)}>Agregar</button>
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
          <button onClick={handleGuardar} className="btn btn-success btn-lg">Crear Sesión</button>
          <Link to="/admin/sesiones" className="btn btn-secondary btn-lg">Volver</Link>
        </div>
      </div>

    </div>
  );
};

export default AdminSesionCrear;
