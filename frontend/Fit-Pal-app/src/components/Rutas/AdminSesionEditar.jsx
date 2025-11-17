import React, { useState, useEffect } from "react";
import CardSesiones from "../Cards/AdminSesiones.jsx";
import AdminSesionEditar from "../Cards/AdminSesionEditar.jsx";

const AdminSesiones = () => {
    const [sesiones, setSesiones] = useState([]);

    useEffect(() => {
        const user = JSON.parse(localStorage.getItem("user"));
        const role = user?.rol;

        if (role !== "administrador") {
            console.error("Acceso denegado: el usuario no es administrador");
            return;
        }

        const url = "http://localhost:5000/api/admin/sesiones";

        fetch(url)
            .then((res) => {
                if (!res.ok) throw new Error(`Error ${res.status}`);
                return res.json();
            })
            .then((data) => {
                if (Array.isArray(data)) setSesiones(data);
                else setSesiones([]);
            })
            .catch(() => setSesiones([]));
    }, []);

    return <AdminSesionEditar sesiones={sesiones} />;

};

export default AdminSesiones;