import React, { useState, useMemo } from "react";
import { Link, useNavigate } from "react-router-dom";

const AdminPlanes = ({ planes }) => {
  const navigate = useNavigate();

  // Estado para búsqueda
  const [search, setSearch] = useState("");

  // Estado para paginación
  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  const safe = (v) => {
    if (v === null || v === undefined) return "";
    return String(v).toLowerCase();
  };

  const handleCrear = () => {
    navigate("/admin/planes/crear");
  };

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
      console.error("Error al eliminar plan:", error);
      alert("No se pudo eliminar el plan.");
    }
  };

  // ---- FILTRADO ----
  const planesFiltrados = useMemo(() => {
    if (!search.trim()) return planes;

    const q = search.trim().toLowerCase();

    return planes.filter(
      (p) =>
        safe(p.nombre).includes(q) ||
        safe(p.frecuencia).includes(q) ||
        safe(p.cliente_id).includes(q)
    );
  }, [search, planes]);

  // ---- PAGINACIÓN ----
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

        {/* Barra de búsqueda */}
        <input
          type="text"
          className="form-control w-50"
          placeholder="Buscar por nombre, frecuencia o cliente..."
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            setPage(1); // igual que en el componente de sesiones
          }}
        />

        {/* Botón crear */}
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
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {planesPaginados.length === 0 ? (
            <tr>
              <td colSpan="4" className="text-center">
                No se encontraron planes.
              </td>
            </tr>
          ) : (
            planesPaginados.map((pl) => (
              <tr key={pl.id}>
                <td>{pl.nombre}</td>
                <td>{pl.frecuencia}</td>
                <td>{pl.cliente_id}</td>

                <td>
                  <Link
                    className="btn btn-primary btn-sm me-2"
                    to={`/admin/planes/${pl.id}/editar`}
                  >
                    Editar
                  </Link>

                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleEliminar(pl.id)}
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      {/* ---- PAGINACIÓN ---- */}
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
