import React, { useState, useMemo } from "react";
import { Link, useNavigate } from "react-router-dom";

const AdminSesiones = ({ sesiones }) => {
  const navigate = useNavigate();

  // Estado para búsqueda
  const [search, setSearch] = useState("");

  // Estado para paginación
  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  const handleCrear = () => {
    navigate("/admin/sesiones/crear");
  };

  const handleEditar = (sesion) => {
    navigate(`/admin/sesiones/${sesion.id}/editar`);
  };

  const handleEliminar = async (id) => {
    const confirmar = window.confirm("¿Seguro que querés eliminar esta sesión?");

    if (!confirmar) return;

    try {
      const res = await fetch(`http://localhost:5000/api/admin/sesiones/${id}`, {
        method: "DELETE",
      });

      if (!res.ok) {
        throw new Error("Error eliminando sesión");
      }

      window.location.reload();
    } catch (error) {
      console.error("Error al eliminar sesión:", error);
      alert("No se pudo eliminar la sesión.");
    }
  };

  // ---- FILTRADO ----
  const sesionesFiltradas = useMemo(() => {
    if (!search.trim()) return sesiones;

    const s = search.toLowerCase();

    return sesiones.filter(
      (ses) =>
        ses.nombre.toLowerCase().includes(s) ||
        (ses.descripcion && ses.descripcion.toLowerCase().includes(s))
    );
  }, [search, sesiones]);

  // ---- PAGINACIÓN ----
  const totalPages = Math.ceil(sesionesFiltradas.length / itemsPerPage);

  const sesionesPaginadas = useMemo(() => {
    const start = (page - 1) * itemsPerPage;
    return sesionesFiltradas.slice(start, start + itemsPerPage);
  }, [page, sesionesFiltradas]);

  const cambiarPagina = (p) => {
    if (p < 1 || p > totalPages) return;
    setPage(p);
  };

  return (
    <div className="container py-4">

      <h1 className="mb-3 text-center">Gestión de Sesiones</h1>

      <div className="d-flex justify-content-between align-items-center mb-3">
        
        {/* Barra de búsqueda */}
        <input
          type="text"
          className="form-control w-50"
          placeholder="Buscar por nombre o descripción..."
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            setPage(1);
          }}
        />

        {/* Botón crear */}
        <button className="btn btn-success" onClick={handleCrear}>
          Crear sesión
        </button>
      </div>

      <table className="table table-striped table-dark">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {sesionesPaginadas.length === 0 ? (
            <tr>
              <td colSpan="4" className="text-center">
                No se encontraron sesiones.
              </td>
            </tr>
          ) : (
            sesionesPaginadas.map((ses) => (
              <tr key={ses.id}>
                <td>{ses.nombre}</td>
                <td>{ses.descripcion}</td>
                <td>{ses.estado ? "Activa" : "Inactiva"}</td>

                <td>
                  <button
                    className="btn btn-primary btn-sm me-2"
                    onClick={() => handleEditar(ses)}
                  >
                    Editar
                  </button>

                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleEliminar(ses.id)}
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

export default AdminSesiones;
