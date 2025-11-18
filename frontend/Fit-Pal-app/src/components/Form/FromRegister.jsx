import { useState } from 'react';
const API = import.meta.env.VITE_API_URL;

const FormRegister = () => {

    const [isRegister, setIsRegister] = useState(false);
    const [showPassword, setShowPassword] = useState(false);

    const [registerData, setRegisterData] = useState({
        name: '',
        lastname: '',
        dni: '',
        edad: '',
        email: '',
        password: ''
    });

    const handleRegisterInputChange = (e) => {
        const { name, value } = e.target;
        setRegisterData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleRegisterSubmit = async (e) => {
        e.preventDefault();
        
        try {
        
            const response = await fetch(`${API}/api/register`, {
                method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
                body: JSON.stringify(registerData),
            });
            
            const data = await response.json();
            
            if (response.ok) {
            alert('Registro exitoso!');

                setIsRegister(false);
            } else {
                alert(`Error: ${data.message || data.error}`);
            }
        } catch {
            alert('Error de conexión con el servidor');
        }
    };
    return (
        <div className="form-box register">
            <form onSubmit={handleRegisterSubmit}>
                <h1>Registrate</h1>
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

                <button type="submit" className="btn-login">Registrarse</button>
            </form>
        </div>
    );
};
export default FormRegister;