import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";

const AdminSesionEditar = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [sesion, setSesion] = useState({ nombre: "", duracion: "", descripcion: "" });
  const [ejerciciosSesion, setEjerciciosSesion] = useState([]);
  const [ejerciciosDisponibles, setEjerciciosDisponibles] = useState([]);

  // Cargar sesión y ejercicios
  useEffect(() => {
    // Datos de la sesión
    fetch(`/api/admin/sesiones/${id}`)
      .then(res => res.json())
      .then(data => setSesion({ nombre: data.nombre, duracion: data.duracion, descripcion: data.descripcion }))
      .catch(console.error);

    // Ejercicios asignados
    fetch(`/api/admin/sesiones/${id}/ejercicios`)
      .then(res => res.json())
      .then(data => setEjerciciosSesion(data))
      .catch(console.error);

    // Todos los ejercicios disponibles
    fetch("/api/admin/ejercicios")
      .then(res => res.json())
      .then(data => setEjerciciosDisponibles(data))
      .catch(console.error);
  }, [id]);

  // Guardar cambios de la sesión
  const handleGuardar = (e) => {
    e.preventDefault();
    fetch(`/api/admin/sesiones/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(sesion),
    })
      .then(res => res.json())
      .then(() => navigate("/admin/sesiones"))
      .catch(console.error);
  };

  // Agregar ejercicio a la sesión
  const agregarEjercicio = (ejId) => {
    fetch(`/api/admin/sesiones/${id}/ejercicios`, {
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

  // Quitar ejercicio de la sesión
  const quitarEjercicio = (ejId) => {
    fetch(`/api/admin/sesiones/${id}/ejercicios/${ejId}`, { method: "DELETE" })
      .then(() => {
        setEjerciciosSesion(ejerciciosSesion.filter(e => e.id !== ejId));
      })
      .catch(console.error);
  };

  return (
    <div className="container py-4">
      <h1 className="mb-4 text-center">Editar Sesión</h1>

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
          <label className="form-label">Duración (minutos)</label>
          <input
            type="number"
            className="form-control"
            value={sesion.duracion}
            onChange={(e) => setSesion({ ...sesion, duracion: e.target.value })}
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

        <button type="submit" className="btn btn-success">Guardar Sesión</button>
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
          <ul className="list-group">
            {ejerciciosDisponibles
              .filter(e => !ejerciciosSesion.some(es => es.id === e.id))
              .map(e => (
                <li key={e.id} className="list-group-item d-flex justify-content-between align-items-center">
                  {e.nombre}
                  <button className="btn btn-sm btn-primary" onClick={() => agregarEjercicio(e.id)}>Agregar</button>
                </li>
              ))}
            {ejerciciosDisponibles.filter(e => !ejerciciosSesion.some(es => es.id === e.id)).length === 0 &&
              <li className="list-group-item">No hay ejercicios disponibles</li>}
          </ul>
        </div>
      </div>

      <div className="text-center mt-4">
        <Link to="/admin/sesiones" className="btn btn-secondary">Volver</Link>
      </div>
    </div>
  );
};

export default AdminSesionEditar;
