import { Navigate } from "react-router-dom"

export const ProtectedUserRoute = ({ children }) => {
    const user = JSON.parse(localStorage.getItem('user'));


    if (!user) {
        return <Navigate to="/login" replace />;
    }

    return children;
}

export const ProtectedAdminRoute = ({ children }) => {
    const userJSON = localStorage.getItem("user");

    if (!userJSON) {
        return <Navigate to="/login" replace />;
    }

    const user = JSON.parse(userJSON);


    if (user.rol !== "administrador") {
        return <Navigate to="/login" replace />;
    }

    return children;
}

