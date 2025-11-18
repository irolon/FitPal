import React, { useState, useMemo } from "react";
import { Link, useNavigate } from "react-router-dom";

const AdminEjercicios = ({ ejercicios }) => {
  const navigate = useNavigate();

  // Estado para búsqueda
  const [search, setSearch] = useState("");

  // Estado para paginación
  const [page, setPage] = useState(1);
  const itemsPerPage = 10;

  const handleCrear = () => {
    navigate("/admin/ejercicios/crear");
  };

  const handleEditar = (ejercicio) => {
    navigate(`/admin/ejercicios/${ejercicio.id}/editar`);
  };

  const handleEliminar = async (id) => {
    const confirmar = window.confirm("¿Seguro que querés eliminar este ejercicio?");

    if (!confirmar) return;

    try {
      const res = await fetch(`http://localhost:5000/api/admin/ejercicios/${id}`, {
        method: "DELETE",
      });

      if (!res.ok) {
        throw new Error("Error eliminando ejercicio");
      }

      window.location.reload();
    } catch (error) {
      console.error("Error al eliminar ejercicio:", error);
      alert("No se pudo eliminar el ejercicio.");
    }
  };

  // ---- FILTRADO ----
  const ejerciciosFiltrados = useMemo(() => {
    if (!search.trim()) return ejercicios;


    const s = search.toLowerCase();

    return ejercicios.filter((e) =>
      e.nombre.toLowerCase().includes(s) ||
      e.categoria.toLowerCase().includes(s) ||
      (e.descripcion && e.descripcion.toLowerCase().includes(s))
    );
  }, [search, ejercicios]);

  // ---- PAGINACIÓN ----
  const totalPages = Math.ceil(ejerciciosFiltrados.length / itemsPerPage);

  const ejerciciosPaginados = useMemo(() => {
    const start = (page - 1) * itemsPerPage;
    return ejerciciosFiltrados.slice(start, start + itemsPerPage);
  }, [page, ejerciciosFiltrados]);

  const cambiarPagina = (p) => {
    if (p < 1 || p > totalPages) return;
    setPage(p);
  };

  return (
    <div className="div-home vh-100 py-4">

      <h1 className="mb-3 text-center">Gestión de Ejercicios</h1>

      <div className="container d-flex justify-content-between align-items-center mb-3">
        
        {/* Barra de búsqueda */}
        <input
          type="text"
          className="form-control w-50"
          placeholder="Buscar por nombre, categoría o descripción..."
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            setPage(1); // Reiniciar a página 1 cuando se busca
          }}
        />

        {/* Botón crear */}
        <button className="btn btn-success" onClick={handleCrear}>
          Crear ejercicio
        </button>
      </div>

      <table className="container table table-striped table-dark">
        <thead>
          <tr>
            <th>Categoria</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Repeticiones</th>
            <th>Series</th>
            <th>Descanso</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {ejerciciosPaginados.length === 0 ? (
            <tr>
              <td colSpan="8" className="text-center">
                No se encontraron ejercicios.
              </td>
            </tr>
          ) : (
            ejerciciosPaginados.map((ej) => (
              <tr key={ej.id}>
                <td>{ej.categoria}</td>
                <td>{ej.nombre}</td>
                <td>{ej.descripcion}</td>
                <td>{ej.repeticiones}</td>
                <td>{ej.series}</td>
                <td>{ej.descanso}</td>


                <td>
                  <button
                    className="btn btn-primary btn-sm me-2"
                    onClick={() => handleEditar(ej)}
                  >
                    Editar
                  </button>

                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleEliminar(ej.id)}
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

export default AdminEjercicios;
