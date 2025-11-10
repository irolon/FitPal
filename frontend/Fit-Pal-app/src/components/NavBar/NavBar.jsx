import '../../css/NavBar.css';
import BtnLogin from '../Btn/BtnLogin';
import { Link, useLocation } from 'react-router-dom';


const NavBar = () => {
    const location = useLocation();
    const isLoginPage = location.pathname === '/login';

    return (
    <nav className="navbar navbar-expand-lg navbar-dark fixed-top">
        <div className="container-fluid px-4 d-flex justify-content-between">

            <div className="logo">

                <a href="/" className="navbar-brand d-flex align-items-center">     
                 <span className="logo-svg" aria-label="marca"></span>
                </a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu"
                    aria-controls="menu" aria-expanded="false" aria-label="Mostrar - Ocultar menu">
                    <span className="navbar-toggler-icon"></span>
                </button>
            </div>
            <div className="collapse navbar-collapse" id="menu">
                <ul className="navbar-nav mx-auto mb-2 mb-lg-0">
                    <li className="nav-item">
                        <Link to="/nosotros" className="nav-link color-nav">Nosotros</Link>
                    </li>

                    <li className="nav-item">
                        <Link to="/planes" className="nav-link color-nav">Plan</Link>
                    </li>

                    <li className="nav-item">
                        <Link to="/novedades" className="nav-link color-nav">Novedades</Link>
                    </li>

                </ul>
            </div>
            <div className="d-flex align-items-center gap-2 position-relative">
                {!isLoginPage && <BtnLogin />}
            </div>
        </div>
    </nav>
    );
}

export default NavBar;
