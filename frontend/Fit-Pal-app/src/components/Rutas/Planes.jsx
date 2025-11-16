import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import CardTablaPlanes from "../Cards/CardTablaPlanes.jsx";

const Planes = () => {
  const { id } = useParams();          // <- esto toma el :id de la ruta
  const [planes, setPlanes] = useState([]);

  useEffect(() => {
    if (!id) return;

    fetch(`http://localhost:5000/api/cliente/${id}/planes`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Error ${res.status}: ${res.statusText}`);
        }
        return res.json();
      })
      .then((data) => {
        // Validar que data sea un array
        if (Array.isArray(data)) {
          setPlanes(data);
        } else {
          console.error("Los datos recibidos no son un array:", data);
          setPlanes([]); // Establecer array vacío como fallback
        }
      })
      .catch((err) => {
        console.error("Error al traer planes:", err);
        setPlanes([]); // Establecer array vacío en caso de error
      });
  }, [id]);

  return (
    <CardTablaPlanes planes={planes} />
  );
};

export default Planes;