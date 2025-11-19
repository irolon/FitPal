import React, { useState, useEffect } from "react";
import CardUsuarios from "../Cards/AdminUsuarios.jsx";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

const AdminUsuarios = () => {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem("user"));
    if (storedUser?.rol !== "administrador") {
      console.error("Acceso denegado: el usuario no es administrador");
      return;
    }

    fetch(`${API_URL}/api/usuarios`)
      .then((res) => {
        if (!res.ok) throw new Error(`Error ${res.status}`);
        return res.json();
      })
      .then((data) => {
        if (Array.isArray(data)) {
          setUsuarios(
            data.map((usuario) => ({
              id: usuario.id,
              nombre: usuario.nombre,
              apellido: usuario.apellido,
              correo: usuario.correo,
              rol: usuario.rol,
              contrasena: usuario.contrasena,
            }))
          );
        } else {
          setUsuarios([]);
        }
      })
      .catch((error) => {
        console.error("No se pudieron cargar los usuarios:", error);
        setUsuarios([]);
      });
  }, []);

  const eliminarUsuario = async (usuarioId) => {
    try {
      const res = await fetch(`${API_URL}/api/usuarios/${usuarioId}`, {
        method: "DELETE",
      });
      if (!res.ok) {
        throw new Error("No se pudo eliminar el usuario");
      }

      setUsuarios((prev) => prev.filter((u) => u.id !== usuarioId));
      return true;
    } catch (error) {
      console.error("Error al eliminar el usuario:", error);
      return false;
    }
  };

  return (
    <CardUsuarios usuarios={usuarios} onDelete={eliminarUsuario} />
  );
};

export default AdminUsuarios;
