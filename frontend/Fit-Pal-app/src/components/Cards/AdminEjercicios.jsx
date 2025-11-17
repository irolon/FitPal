
import React from "react";
import { Link, useNavigate } from "react-router-dom";

const AdminEjercicios = ({ ejercicios }) => {
  const navigate = useNavigate();

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

      window.location.reload(); // recargar para actualizar la lista
    } catch (error) {
      console.error("Error al eliminar ejercicio:", error);
      alert("No se pudo eliminar el ejercicio.");
    }
  };

  return (
    <div className="container vh-100 d-flex flex-column align-items-center justify-content-center">
      <h1 className="mb-4">Gestión de Ejercicios (Admin)</h1>
      <p>Aquí podés administrar los ejercicios del sistema.</p>

      <div className="d-flex justify-content-end w-100 mb-3">
        <button className="btn btn-success" onClick={handleCrear}>
          Crear ejercicio
        </button>
      </div>

      <table className="table table-striped table-dark">
        <thead>
          <tr>
            <th>Categoria</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Repeticiones</th>
            <th>Series</th>
            <th>Descanso</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {ejercicios.length === 0 ? (
            <tr>
              <td colSpan="8" className="text-center">
                No hay ejercicios cargados.
              </td>
            </tr>
          ) : (
            ejercicios.map((ej) => (
              <tr key={ej.id}>
                <td>{ej.categoria}</td>
                <td>{ej.nombre}</td>
                <td>{ej.descripcion}</td>
                <td>{ej.repeticiones}</td>
                <td>{ej.series}</td>
                <td>{ej.descanso}</td>

                <td>
                  <span
                    className={`badge ${
                      ej.estado === "Activo"
                        ? "bg-success"
                        : ej.estado === "Inactivo"
                        ? "bg-secondary"
                        : "bg-warning"
                    }`}
                  >
                    {ej.estado}
                  </span>
                </td>

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

      <div>
        <Link to="/admin" className="btn btn-success mt-4">
          Volver al panel admin
        </Link>
      </div>
    </div>
  );
};

export default AdminEjercicios;
