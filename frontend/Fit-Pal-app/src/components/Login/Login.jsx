import { useState } from 'react';
import '../../css/login.css';
import FormLogin from '../Form/FormLogin';
import FormRegister from '../Form/FromRegister.jsx';
import CardToggle from '../Cards/CardToggle.jsx';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [isRegister, setIsRegister] = useState(false);
    const [showForgotModal, setShowForgotModal] = useState(false);
    const navigate = useNavigate();

    return (
        <>
            <div className="min-vh-100 d-flex align-items-center justify-content-center">
                <div className={`div-container-login ${isRegister ? "active" : ""}`}>
                    
                    <FormLogin 
                        navigate={navigate}
                        onForgotPassword={() => setShowForgotModal(true)}
                    />

                    <FormRegister 
                        navigate={navigate}
                        setIsRegister={setIsRegister}
                    />
                    <CardToggle 
                        isRegister={isRegister} 
                        setIsRegister={setIsRegister} 
                    />
                </div>
            </div>

            {showForgotModal && (
                <div className="fp-modal-overlay">
                    <div className="fp-modal">
                        <h5 className="fp-modal-title">Recuperar contraseña</h5>
                        <p className="fp-modal-text">
                            Para recuperar tu contraseña, comunicate con Administración.
                        </p>
                        <p className="fp-modal-text fp-modal-email">
                            administracion@fitpal.com
                        </p>
                        <button 
                            className="btn-fitpal fp-modal-button"
                            onClick={() => setShowForgotModal(false)}
                        >
                            Entendido
                        </button>
                    </div>
                </div>
            )}
        </>
    );
};

export default Login;

