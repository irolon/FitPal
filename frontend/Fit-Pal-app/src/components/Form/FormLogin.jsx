import { useState } from 'react';
const API = import.meta.env.VITE_API_URL;

const FormLogin = ({ navigate }) => {
        // Estados para el formulario de login
        const [username, setUsername] = useState('');
        const [password, setPassword] = useState('');
        const [errorMessage, setErrorMessage] = useState('');


        const handleLoginSubmit = async (e) => {
        e.preventDefault();
        
        // Validación en el frontend
        if (!username || !password) {
            setErrorMessage('Por favor ingresa usuario y contraseña');
            return;
        }
        
        try {
            
            const response = await fetch(`${API}/api/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });
            
            const data = await response.json();
            console.log('Respuesta del servidor:', data);
            
            if (response.ok && data.rol === 'cliente') {
                localStorage.setItem('user', JSON.stringify(data));
                navigate('/cliente');
            } else if (response.ok && data.rol === 'administrador') {
                localStorage.setItem('user', JSON.stringify(data));
                navigate('/admin');
            } else {
                setErrorMessage(`Usuario o contraseña incorrectos`);
            }
        } catch (error) {
            console.error('Error de conexión:', error);
            setErrorMessage('Error de conexión con el servidor');
        }
    };

    return (
        <div className="form-box login">
            <form onSubmit={handleLoginSubmit}>
                <h1>Inicio de Sesion</h1>
                {errorMessage && <div className="alert alert-danger mt-5" role="alert">{errorMessage}</div>}
                <div className="input-box">
                    <input type="text" id="username" name="username" placeholder='Usuario' value={username} onChange={(e) => setUsername(e.target.value)}  />
                    <i className='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input type="password" id="password" name="password" placeholder='Contraseña' value={password} onChange={(e) => setPassword(e.target.value)} />
                    <i className='bx bxs-lock'></i>
                </div>
                <div className="forgot-link">
                    <a href="#">Olvidar contraseña</a>
                </div>
                <button type="submit" className="btn-login" >Login</button>
            </form>
        </div>




    );
}

export default FormLogin;