import React, { useState, useEffect } from "react";
import CardEjercicios from "../Cards/AdminEjercicios.jsx";

const AdminEjercicios = () => {
    const [ejercicios, setEjercicios] = useState([]);

    useEffect(() => {
        const user = JSON.parse(localStorage.getItem("user"));
        const role = user?.rol;

        if (role !== "administrador") {
            console.error("Acceso denegado: el usuario no es administrador");
            return;
        }

        const url = "http://localhost:5000/api/admin/ejercicios";

        fetch(url)
            .then((res) => {
                if (!res.ok) throw new Error(`Error ${res.status}`);
                return res.json();
            })
            .then((data) => {
                if (Array.isArray(data)) setEjercicios(data);
                else setEjercicios([]);
            })
            .catch(() => setEjercicios([]));
    }, []);

    return <CardEjercicios ejercicios={ejercicios} />;
};

export default AdminEjercicios;