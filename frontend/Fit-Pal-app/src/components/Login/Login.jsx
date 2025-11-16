import { useState } from 'react';
import '../../css/login.css';
import FormLogin from '../Form/FormLogin';
import FormRegister from '../Form/FromRegister.jsx';
import CardToggle from '../Cards/CardToggle.jsx';
import {useNavigate} from 'react-router-dom';

const Login = () => {

    const [isRegister, setIsRegister] = useState(false);
    const navigate = useNavigate();

    return (
            <div className="min-vh-100 d-flex align-items-center justify-content-center">
                <div className={`div-container-login ${isRegister ? "active" : ""}`}>
                    <FormLogin navigate={navigate} />
                    <FormRegister />
                    <CardToggle isRegister={isRegister} setIsRegister={setIsRegister} />


                </div>
            </div>
        );
};
export default Login;