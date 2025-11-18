import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";

const EditarEjercicio = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [form, setForm] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5000/api/admin/ejercicios/${id}`)
      .then((res) => res.json())
      .then((data) => setForm(data))
      .catch(() => alert("Error cargando el ejercicio"));
  }, [id]);

  if (!form) return <p className="text-center mt-5">Cargando...</p>;

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch(
        `http://localhost:5000/api/admin/ejercicios/${id}`,
        {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        }
      );

      if (!res.ok) throw new Error("Error al actualizar ejercicio");

      navigate("/admin/ejercicios");
    } catch (err) {
      console.error(err);
      alert("No se pudo actualizar el ejercicio.");
    }
  };

  return (
    <div className="div-home vh-100 py-4">
      <div className="container">
        <h2>Editar Ejercicio</h2>

        <form onSubmit={handleSubmit} className="mt-3">
          <div className="mb-3">
            <label className="form-label">Categoria</label>
            <input
              type="text"
              name="categoria"
              className="form-control"
              value={form.categoria}
              onChange={handleChange}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Nombre</label>
            <input
              type="text"
              name="nombre"
              className="form-control"
              value={form.nombre}
              onChange={handleChange}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Descripción</label>
            <textarea
              name="descripcion"
              className="form-control"
              value={form.descripcion}
              onChange={handleChange}
            ></textarea>
          </div>

          <div className="row">
            <div className="col mb-3">
              <label className="form-label">Repeticiones</label>
              <input
                type="number"
                name="repeticiones"
                className="form-control"
                value={form.repeticiones}
                onChange={handleChange}
              />
            </div>

            <div className="col mb-3">
              <label className="form-label">Series</label>
              <input
                type="number"
                name="series"
                className="form-control"
                value={form.series}
                onChange={handleChange}
              />
            </div>

            <div className="col mb-3">
              <label className="form-label">Descanso (seg)</label>
              <input
                type="number"
                name="descanso"
                className="form-control"
                value={form.descanso}
                onChange={handleChange}
              />
            </div>
          </div>

          <button type="submit" className="btn btn-primary">
            Guardar cambios
          </button>

          <button
            type="button"
            className="btn btn-secondary ms-3"
            onClick={() => navigate("/admin/ejercicios")}
          >
            Cancelar
          </button>
        </form>
      </div>

    </div>
  );
};

export default EditarEjercicio;
