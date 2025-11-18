import React, { useState, useMemo } from "react";
import { Link, useNavigate } from "react-router-dom";

const AdminPlanes = ({ planes }) => {
  const navigate = useNavigate();

  const [search, setSearch] = useState("");
  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  const handleEliminar = async (id) => {
    const confirmar = window.confirm("¿Seguro que querés eliminar este plan?");
    if (!confirmar) return;

    try {
      const res = await fetch(`http://localhost:5000/api/admin/planes/${id}`, {
        method: "DELETE",
      });

      if (!res.ok) throw new Error("Error eliminando plan");

      window.location.reload();
    } catch (error) {
      console.error("Error:", error);
      alert("No se pudo eliminar el plan.");
    }
  };

  // --- FILTRADO ---
  const planesFiltrados = useMemo(() => {
    if (!search.trim()) return planes;

    const s = search.toLowerCase();

    return planes.filter(
      (p) =>
        p.nombre.toLowerCase().includes(s) ||
        (p.frecuencia && p.frecuencia.toLowerCase().includes(s))
    );
  }, [search, planes]);

  // --- PAGINACIÓN ---
  const totalPages = Math.ceil(planesFiltrados.length / itemsPerPage);

  const planesPaginados = useMemo(() => {
    const start = (page - 1) * itemsPerPage;
    return planesFiltrados.slice(start, start + itemsPerPage);
  }, [page, planesFiltrados]);

  const cambiarPagina = (p) => {
    if (p < 1 || p > totalPages) return;
    setPage(p);
  };

  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-3 text-center">Gestión de Planes</h1>

      <div className="container d-flex justify-content-between align-items-center mb-3">
        <input
          type="text"
          className="form-control w-50"
          placeholder="Buscar por nombre o frecuencia..."
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            setPage(1);
          }}
        />

        <Link className="btn btn-success" to="/admin/planes/crear">
          Crear
        </Link>
      </div>

      <table className="container table table-striped table-dark">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Frecuencia</th>
            <th>Cliente</th>
            <th>Inicio</th>
            <th>Fin</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {planesPaginados.length === 0 ? (
            <tr>
              <td colSpan="6" className="text-center">
                No se encontraron planes.
              </td>
            </tr>
          ) : (
            planesPaginados.map((p) => (
              <tr key={p.id}>
                <td>{p.nombre}</td>
                <td>{p.frecuencia}</td>
                <td>{p.cliente_id}</td>
                <td>{p.fecha_inicio}</td>
                <td>{p.fecha_fin}</td>

                <td>
                  <Link
                    className="btn btn-primary btn-sm me-2"
                    to={`/admin/planes/${p.id}/editar`}
                  >
                    Editar
                  </Link>

                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleEliminar(p.id)}
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      {totalPages > 1 && (
        <div className="d-flex justify-content-center mt-3">
          <button
            className="btn btn-outline-dark me-2"
            onClick={() => cambiarPagina(page - 1)}
            disabled={page === 1}
          >
            Anterior
          </button>

          <span className="px-3 align-self-center">
            Página {page} de {totalPages}
          </span>

          <button
            className="btn btn-outline-dark ms-2"
            onClick={() => cambiarPagina(page + 1)}
            disabled={page === totalPages}
          >
            Siguiente
          </button>
        </div>
      )}

      <div className="text-center mt-4">
        <Link to="/admin" className="btn btn-success">
          Volver al panel admin
        </Link>
      </div>
    </div>
  );
};

export default AdminPlanes;
