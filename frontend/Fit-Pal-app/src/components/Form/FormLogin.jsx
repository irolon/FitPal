import { useState } from 'react';
const API = import.meta.env.VITE_API_URL;

const FormLogin = ({ navigate, onForgotPassword }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [showPassword, setShowPassword] = useState(false);

    const handleLoginSubmit = async (e) => {
        e.preventDefault();

        if (!username || !password) {
            setErrorMessage('Por favor ingresa usuario y contraseña');
            return;
        }

        try {
            const response = await fetch(`${API}/api/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (response.ok && data.rol === 'cliente') {
                localStorage.setItem('user', JSON.stringify(data));
                navigate('/cliente');
            } else if (response.ok && data.rol === 'administrador') {
                localStorage.setItem('user', JSON.stringify(data));
                navigate('/admin');
            } else {
                setErrorMessage('Usuario o contraseña incorrectos');
            }

        } catch {
            setErrorMessage('Error de conexión con el servidor');
        }
    };

    return (
        <div className="form-box login">
            <form onSubmit={handleLoginSubmit}>
                <h1>Inicio de Sesión</h1>

                {errorMessage && (
                    <div className="alert alert-danger mt-5">{errorMessage}</div>
                )}

                <div className="input-box">
                    <input 
                        type="text" 
                        placeholder="Usuario"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <i className='bx bxs-user'></i>
                </div>

                <div className="input-box">
                    <input 
                        type={showPassword ? "text" : "password"}
                        placeholder="Contraseña"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <i 
                        className={`bx ${showPassword ? 'bx-hide' : 'bx-show'} password-toggle`}
                        onClick={() => setShowPassword(!showPassword)}
                    ></i>
                </div>

                <div className="forgot-link">
                    <button 
                        type="button" 
                        className="btn-link-forgot"
                        onClick={onForgotPassword}
                    >
                        Olvidé mi contraseña
                    </button>
                </div>

                <button type="submit" className="btn-login">
                    Acceder
                </button>
            </form>
        </div>
    );
};

export default FormLogin;
