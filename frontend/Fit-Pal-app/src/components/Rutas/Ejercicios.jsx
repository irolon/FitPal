import React, { use } from 'react'
import { useParams } from "react-router-dom";
import { useState, useEffect } from 'react';
import CardEjercicios from '../Cards/CardEjercicios.jsx';

const Ejercicios = () => {
    const { id } = useParams();  
    const [ejercicios, setEjercicios] = useState([]);

    useEffect(() => {
      if (!id) {
        console.log("No hay ID de cliente");
        return;
      }  
      const url = `http://localhost:5000/api/cliente/${id}/ejercicios`;
        
      fetch(`http://localhost:5000/api/cliente/${id}/ejercicios`)
        .then((res) => {
            if (!res.ok) {
                throw new Error(`Error ${res.status}: ${res.statusText}`);
            }
            return res.json();
        })
        .then((data) => {
            if (Array.isArray(data)) {
                setEjercicios(data);
            } else {
                setEjercicios([]);
            }
        })
        .catch((error) => {
            console.error("Error fetching ejercicios:", error);
            setEjercicios([]);
        });
    }, [id]);

  return (
    <CardEjercicios ejercicios={ejercicios} clienteId={id} />
  )
}

export default Ejercicios