import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import CardTablaSesiones from "../Cards/CardTablaSesiones.jsx";

const Sesiones = () => {
    const { id } = useParams();  
    const [sesiones, setSesiones] = useState([]);

    useEffect(() => {
      if (!id) return;

        fetch(`http://localhost:5000/api/plan_sesion/cliente/${id}/sesiones`)
        .then((res) => {
            if (!res.ok) {
                throw new Error(`Error ${res.status}: ${res.statusText}`);
            }
            return res.json();
        })
        .then((data) => {
            if (Array.isArray(data)) {
                setSesiones(data);
                console.log(data);
                console.log(sesiones);
                
            } else {
                console.error("Datos de sesiones no son un array:", data);
                setSesiones([]);
            }
        })
        .catch((error) => {
            console.error("Error al obtener sesiones:", error);
        });
    }, [id]);





  return (
    <CardTablaSesiones sesiones={sesiones} clienteId={id} />
  )
}

export default Sesiones