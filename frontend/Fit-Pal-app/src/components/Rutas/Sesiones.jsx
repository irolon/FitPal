import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import CardTablaSesiones from "../Cards/CardTablaSesiones.jsx";

const Sesiones = () => {
    const { id } = useParams();  // <- esto toma el :id de la ruta
    const [sesiones, setSesiones] = useState([]);

    useEffect(() => {
      if (!id) return;

        fetch(`http://localhost:5000/api/cliente/${id}/sesiones`)
        .then((res) => {
            if (!res.ok) {
                throw new Error(`Error ${res.status}: ${res.statusText}`);
            }
            return res.json();
        })
        .then((data) => {
            // Validar que data sea un array
            if (Array.isArray(data)) {
                setSesiones(data);
            } else {
                console.error("Datos de sesiones no son un array:", data);
            }
        })
        .catch((error) => {
            console.error("Error al obtener sesiones:", error);
        });
    }, [id]);





  return (
    <CardTablaSesiones sesiones={sesiones} />
  )
}

export default Sesiones