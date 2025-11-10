import { useState } from 'react';

const CardToggle = ({ isRegister, setIsRegister }) => {


    return (
        <div className="toggle-box">
            <div className="toggle-panel toggle-left">
                <h1>
                    Bienvenido
                </h1>
                <p>Todavia no estas registrado?</p>
                <button className="btn register-btn" onClick={() => setIsRegister(prev => !prev)}>Registrate</button>
            </div>
            <div className="toggle-panel toggle-right">
                <h1>
                    Bienvenido
                </h1>
                <p>Tenes una cuenta?</p>
                <button className=" login-btn" onClick={() => setIsRegister(prev => !prev)}>Iniciar Sesion</button>
            </div>
        </div>        

    );
};

export default CardToggle;