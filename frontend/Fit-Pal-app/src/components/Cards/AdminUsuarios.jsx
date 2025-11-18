import React, { useMemo, useState } from "react";
import { Link } from "react-router-dom";

const AdminUsuarios = ({ usuarios, onDelete }) => {
  const [search, setSearch] = useState("");
  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  const usuariosFiltrados = useMemo(() => {
    if (!search.trim()) return usuarios;

    const criterio = search.toLowerCase();
    return usuarios.filter((usuario) => {
      return (
        usuario.nombre?.toLowerCase().includes(criterio) ||
        usuario.apellido?.toLowerCase().includes(criterio) ||
        usuario.correo?.toLowerCase().includes(criterio) ||
        usuario.rol?.toLowerCase().includes(criterio)
      );
    });
  }, [search, usuarios]);

  const totalPages =
    usuariosFiltrados.length > 0
      ? Math.ceil(usuariosFiltrados.length / itemsPerPage)
      : 1;

  const usuariosPaginados = useMemo(() => {
    const start = (page - 1) * itemsPerPage;
    return usuariosFiltrados.slice(start, start + itemsPerPage);
  }, [page, usuariosFiltrados]);

  const cambiarPagina = (nuevaPagina) => {
    if (nuevaPagina < 1 || nuevaPagina > totalPages) return;
    setPage(nuevaPagina);
  };

  const handleEliminar = async (usuarioId) => {
    const confirmar = window.confirm(
      "¿Seguro que querés eliminar este usuario?"
    );
    if (!confirmar) {
      return;
    }

    const eliminado = await onDelete?.(usuarioId);
    if (!eliminado) {
      alert("No se pudo eliminar el usuario. Intentalo nuevamente.");
    }
  };

  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-3 text-center">Gestión de Usuarios</h1>

      <div className="container d-flex justify-content-between align-items-center mb-3">
        <input
          type="text"
          className="form-control w-50"
          placeholder="Buscar por nombre, apellido o correo..."
          value={search}
          onChange={(event) => {
            setSearch(event.target.value);
            setPage(1);
          }}
        />

        <button
          type="button"
          className="btn btn-success"
          onClick={() =>
            alert("La creación y edición de usuarios estará disponible pronto.")
          }
        >
          Crear
        </button>
      </div>

      <table className="container table table-striped table-dark">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Correo</th>
            <th>Rol</th>
            <th>Contraseña</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {usuariosPaginados.length === 0 ? (
            <tr>
              <td colSpan="7" className="text-center">
                No se encontraron usuarios.
              </td>
            </tr>
          ) : (
            usuariosPaginados.map((usuario) => (
              <tr key={usuario.id}>
                <td>{usuario.id}</td>
                <td>{usuario.nombre}</td>
                <td>{usuario.apellido}</td>
                <td>{usuario.correo}</td>
                <td>{usuario.rol}</td>
                <td>{usuario.contrasena}</td>
                <td>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleEliminar(usuario.id)}
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

export default AdminUsuarios;
