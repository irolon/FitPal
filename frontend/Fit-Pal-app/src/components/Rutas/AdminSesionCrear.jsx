import React, { useState, useEffect } from "react";
import AdminSesionCrear from "../Cards/AdminSesionCrear.jsx";

const AdminSesionCrearWrapper = () => {
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

    return <AdminSesionCrear sesiones={sesiones} />;
};

export default AdminSesionCrearWrapper;
