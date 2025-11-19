import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import FormEditarPlanes from "../Form/FormEditarPlanes";

const AdminPlanEditar = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [plan, setPlan] = useState({ nombre: "", frecuencia: "", fecha_inicio: "", fecha_fin: "", cliente_id: "", administrador_id: "" });
  const [sesiones, setSesiones] = useState([]);
  const [sesionesDisponibles, setSesionesDisponibles] = useState([]);
  const [mostrarModal, setMostrarModal] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:5000/api/admin/planes/${id}`)
      .then(res => res.json())
      .then(data =>
        setPlan({ 
          nombre: data.nombre, 
          frecuencia: data.frecuencia,
          fecha_inicio: data.fecha_inicio || "",
          fecha_fin: data.fecha_fin || "",
          cliente_id: data.cliente_id,
          administrador_id: data.administrador_id
        })
      )
      .catch(console.error);

    // Cargar sesiones del plan
    fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones`)
      .then(res => res.json())
      .then(data => setSesiones(data))
      .catch(console.error);
  }, [id]);

  const cargarSesionesDisponibles = () => {
    fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones/disponibles`)
      .then(res => res.json())
      .then(data => {
        // Asegurar que data sea un array
        if (Array.isArray(data)) {
          setSesionesDisponibles(data);
        } else {
          console.error('Datos de sesiones no válidos:', data);
          setSesionesDisponibles([]);
        }
      })
      .catch(error => {
        console.error('Error al cargar sesiones disponibles:', error);
        setSesionesDisponibles([]);
      });
  };

  const handleGuardar = (e) => {
    e.preventDefault();

    fetch(`http://localhost:5000/api/admin/planes/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(plan),
    })
      .then(res => res.json())
      .then(() => navigate("/admin/planes"))
      .catch(console.error);
  };

  const handleEliminarSesion = async (sesionId) => {
    const confirmar = window.confirm("¿Estás seguro de que quieres eliminar esta sesión del plan?");
    
    if (!confirmar) return;

    try {
      const response = await fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones/${sesionId}`, {
        method: "DELETE"
      });

      if (response.ok) {
        // Actualizar lista de sesiones
        setSesiones(sesiones.filter(s => s.sesion_id !== sesionId));
        alert("Sesión eliminada del plan exitosamente");
      } else {
        alert("Error al eliminar la sesión del plan");
      }
    } catch (error) {
      console.error("Error al eliminar sesión:", error);
      alert("Error al eliminar la sesión del plan");
    }
  };

  const handleAbrirModal = () => {
    cargarSesionesDisponibles();
    setMostrarModal(true);
  };

  const handleCerrarModal = () => {
    setMostrarModal(false);
    setSesionesDisponibles([]);
  };

  const handleAgregarSesion = async (sesionId) => {
    try {
      const response = await fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones/${sesionId}`, {
        method: "POST"
      });

      if (response.ok) {
        // Recargar sesiones del plan
        fetch(`http://localhost:5000/api/admin/planes/${id}/sesiones`)
          .then(res => res.json())
          .then(data => setSesiones(data))
          .catch(console.error);
        
        handleCerrarModal();
        alert("Sesión agregada al plan exitosamente");
      } else {
        alert("Error al agregar la sesión al plan");
      }
    } catch (error) {
      console.error("Error al agregar sesión:", error);
      alert("Error al agregar la sesión al plan");
    }
  };



  return (
    <div className="div-home vh-100 py-4">
      <h1 className="mb-4 text-center">Editar Plan</h1>

      <FormEditarPlanes
        plan={plan}
        setPlan={setPlan}
        handleGuardar={handleGuardar}
        sesiones={sesiones}
        handleAbrirModal={handleAbrirModal}
        handleEliminarSesion={handleEliminarSesion}
        mostrarModal={mostrarModal}
        handleCerrarModal={handleCerrarModal}
        sesionesDisponibles={sesionesDisponibles}
        handleAgregarSesion={handleAgregarSesion}
      />
    </div>
  );
};

export default AdminPlanEditar;
