import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import CardTablaPlanes from "../Cards/CardTablaPlanes.jsx";

const Planes = () => {
  const { id } = useParams();        
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
        if (Array.isArray(data)) {
          setPlanes(data);
        } else {
          console.error("Los datos recibidos no son un array:", data);
          setPlanes([]); 
        }
      })
      .catch((err) => {
        console.error("Error al traer planes:", err);
        setPlanes([]); 
      });
  }, [id]);

  return (
    <CardTablaPlanes planes={planes} />
  );
};

export default Planes;