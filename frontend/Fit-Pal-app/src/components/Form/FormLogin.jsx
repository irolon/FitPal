import { useState } from 'react';
const API = import.meta.env.VITE_API_URL;

const FormLogin = () => {
        // Estados para el formulario de login
        const [username, setUsername] = useState('');
        const [password, setPassword] = useState('');


        const handleLoginSubmit = async (e) => {
        e.preventDefault();
        
        // Validación en el frontend
        if (!username || !password) {
            alert('Por favor ingresa usuario y contraseña');
            return;
        }
        
        try {
            console.log('API URL:', API); // Debug URL
            console.log('Enviando datos de login:', { username, password }); // Debug
            console.log('URL completa:', `${API}/api/login`); // Debug URL completa
            
            const response = await fetch(`${API}/api/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });
            
            const data = await response.json();
            console.log('Respuesta del servidor:', data);
            
            if (response.ok) {
                alert('Login exitoso!');
                // Aquí puedes redirigir al usuario o guardar el token
            } else {
                alert(`Error: ${data.message || data.error}`);
            }
        } catch (error) {
            console.error('Error de conexión:', error);
            alert('Error de conexión con el servidor');
        }
    };

    return (
        <div className="form-box login">
            <form onSubmit={handleLoginSubmit}>
                <h1>Inicio de Sesion</h1>
                <div className="input-box">
                    <input type="text" id="username" name="username" placeholder='Usuario' value={username} onChange={(e) => setUsername(e.target.value)} required />
                    <i className='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input type="password" id="password" name="password" placeholder='Contraseña' value={password} onChange={(e) => setPassword(e.target.value)} required/>
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