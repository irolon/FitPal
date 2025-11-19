import React, { useState, useEffect } from "react";
import AdminPlanes from "../Cards/AdminPlanes.jsx";

const CardAdminPlanes = () => {
    const [planes, setPlanes] = useState([]);

    useEffect(() => {
        const user = JSON.parse(localStorage.getItem("user"));
        const role = user?.rol;

        if (role !== "administrador") {
            console.error("Acceso denegado: el usuario no es administrador");
            return;
        }

        const url = "http://localhost:5000/api/admin/planes";

        fetch(url)
            .then((res) => {
                if (!res.ok) throw new Error(`Error ${res.status}`);
                return res.json();
            })
            .then((data) => {
                if (Array.isArray(data)) setPlanes(data);
                else setPlanes([]);
            })
            .catch(() => setPlanes([]));
    }, []);

    return <AdminPlanes planes={planes} />;
};

export default CardAdminPlanes;
