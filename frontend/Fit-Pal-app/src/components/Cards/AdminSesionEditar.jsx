import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";

const AdminSesionEditar = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [sesion, setSesion] = useState({ nombre: "", descripcion: "" });
  const [ejerciciosSesion, setEjerciciosSesion] = useState([]);
  const [ejerciciosDisponibles, setEjerciciosDisponibles] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  useEffect(() => {
    fetch(`http://localhost:5000/api/admin/sesiones/${id}`)
      .then(res => res.json())
      .then(data => setSesion({ nombre: data.nombre, descripcion: data.descripcion }))
      .catch(console.error);

    fetch(`http://localhost:5000/api/sesion_ejercicio/${id}`)
      .then(res => res.json())
      .then(data => setEjerciciosSesion(data))
      .catch(console.error);

    fetch("http://localhost:5000/api/admin/ejercicios")
      .then(res => res.json())
      .then(data => setEjerciciosDisponibles(data))
      .catch(console.error);
  }, [id]);

  const handleGuardar = (e) => {
    e.preventDefault();
    fetch(`http://localhost:5000/api/admin/sesiones/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(sesion),
    })
      .then(res => res.json())
      .then(() => navigate("/admin/sesiones"))
      .catch(console.error);
  };

  const agregarEjercicio = (ejId) => {
    fetch(`http://localhost:5000/api/sesion_ejercicio/${id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ejercicio_id: ejId }),
    })
      .then(() => {
        const ej = ejerciciosDisponibles.find(e => e.id === ejId);
        setEjerciciosSesion([...ejerciciosSesion, ej]);
      })
      .catch(console.error);
  };

  const quitarEjercicio = (ejId) => {
    fetch(`http://localhost:5000/api/sesion_ejercicio/${id}/${ejId}`, { method: "DELETE" })
      .then(() => {
        setEjerciciosSesion(ejerciciosSesion.filter(e => e.id !== ejId));
      })
      .catch(console.error);
  };

  // Filtrar ejercicios disponibles
  const ejerciciosFiltrados = ejerciciosDisponibles
    .filter(e => !ejerciciosSesion.some(es => es.id === e.id))
    .filter(e => e.nombre.toLowerCase().includes(searchTerm.toLowerCase()));

  // Paginación
  const totalPages = Math.ceil(ejerciciosFiltrados.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const currentItems = ejerciciosFiltrados.slice(startIndex, startIndex + itemsPerPage);

  const cambiarPagina = (pagina) => {
    if (pagina >= 1 && pagina <= totalPages) {
      setCurrentPage(pagina);
    }
  };

  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-4 text-center">Editar Sesión</h1>
      <div className="container">
        <form onSubmit={handleGuardar} className="mb-4">
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


        </form>

        <div className="row">
          <div className="col-md-6">
            <h4>Ejercicios Asignados</h4>
            <ul className="list-group">
              {ejerciciosSesion.map(e => (
                <li key={e.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {e.nombre}
                  <button className="btn btn-sm btn-danger" onClick={() => quitarEjercicio(e.id)}>Quitar</button>
                </li>
              ))}
              {ejerciciosSesion.length === 0 && <li className="list-group-item">No hay ejercicios asignados</li>}
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
                  <button className="btn btn-sm btn-primary" onClick={() => agregarEjercicio(e.id)}>Agregar</button>
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
          <button onClick={handleGuardar} className="btn btn-success btn-lg">Guardar Cambios</button>
          <Link to="/admin/sesiones" className="btn btn-secondary btn-lg">Volver</Link>
        </div>
      </div>
      
    </div>
  );
};

export default AdminSesionEditar;
