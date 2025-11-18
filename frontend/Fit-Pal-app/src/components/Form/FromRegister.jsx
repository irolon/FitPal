import { useState } from 'react';
const API = import.meta.env.VITE_API_URL;

const FormRegister = ({ navigate, setIsRegister }) => {
    const [infoMessage, setInfoMessage] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    const [registerData, setRegisterData] = useState({
        name: '',
        lastname: '',
        dni: '',
        edad: '',
        email: '',
        password: ''
    });

     const handleInfoMessage = () => {
        setInfoMessage('Registro exitoso!');
    }

    const handleRegisterInputChange = (e) => {
        const { name, value } = e.target;
        setRegisterData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleRegisterSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        
        try {
            const registerResponse = await fetch(`${API}/api/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(registerData),
            });
            
            const registerData_response = await registerResponse.json();
            
            if (registerResponse.ok) {
                setInfoMessage('¡Registro exitoso! Ahora puedes iniciar sesión.');
                
                // Cambiar automáticamente a la vista de login después de 2 segundos
                setTimeout(() => {
                    setIsRegister(false); // Esto cambia a la vista de "Iniciar Sesión"
                }, 2000);
                
            } else {
                alert(`Error en el registro: ${registerData_response.message || registerData_response.error}`);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión con el servidor');
        } finally {
            setIsLoading(false);
        }
    };
    return (
        <div className="d-flex flex-column form-box register">

            <form onSubmit={handleRegisterSubmit}>
                <h1>Registrate</h1>
                            {infoMessage && (
                <div className="alert alert-success text-center mt-4">
                    {infoMessage}
                </div>
            )}
                <div className="input-box">
                    <input 
                        type="text"
                        id="name"
                        name="name"
                        placeholder="Nombre"
                        value={registerData.name}
                        onChange={handleRegisterInputChange}
                        required
                    />
                    <i className='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input 
                        type="text"
                        id="lastname"
                        name="lastname"
                        placeholder="Apellido"
                        value={registerData.lastname}
                        onChange={handleRegisterInputChange}
                        required
                    />
                    <i className='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input 
                        type="text"
                        id="dni"
                        name="dni"
                        placeholder="DNI"
                        value={registerData.dni}
                        onChange={handleRegisterInputChange}
                        required
                    />
                    <i className='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input 
                        type="number"
                        id="edad"
                        name="edad"
                        placeholder="Edad"
                        value={registerData.edad}
                        onChange={handleRegisterInputChange}
                        required
                    />
                    <i className='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input 
                        type="email"
                        id="email"
                        name="email"
                        placeholder="Correo Electrónico"
                        value={registerData.email}
                        onChange={handleRegisterInputChange}
                        required
                    />
                    <i className='bx bxs-envelope'></i>
                </div>
                <div className="input-box">
                    <input 
                        type={showPassword ? "text" : "password"}
                        id="registerPassword"
                        name="password"
                        placeholder="Contraseña"
                        value={registerData.password}
                        onChange={handleRegisterInputChange}
                        required
                    />
                    <i 
                        className={`bx ${showPassword ? 'bx-hide' : 'bx-show'} password-toggle`}
                        onClick={() => setShowPassword(!showPassword)}
                    ></i>
                </div>

                <button 
                    type="submit" 
                    className="btn-login" 
                    disabled={isLoading}
                    onClick={handleInfoMessage}
                >
                    {isLoading ? 'Registrando...' : 'Registrarse'}
                </button>
            </form>
        </div>
    );
};
export default FormRegister;