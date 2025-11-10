import '../../css/style.css';
const CardsInicio = () => {

    const imgUrl1 = new URL(`../../assets/img/img-1.jpg`, import.meta.url).href;
    const imgUrl2 = new URL(`../../assets/img/img-2.jpg`, import.meta.url).href;
    const imgUrl3 = new URL(`../../assets/img/img-3.jpg`, import.meta.url).href;
    const imgUrl4 = new URL(`../../assets/img/img-4.jpg`, import.meta.url).href;

    return (
        <div className="row justify-content-center div-cards-inicio">
            <div className="col-12 col-sm-6 col-md-3 mb-5 px-3 div-card">
                <div className="card h-100 border-0 card-box">
                    <img src={imgUrl1} className="card-img-top" alt={'img-entrenamiento'} />
                    <div className="card-body d-flex flex-column align-items-center ">
                        <h5 className="card-title">Planes Personalizados</h5>
                        <p className="card-text text-center">Cada usuario recibe un plan ajustado a su objetivo: ganar masa muscular, bajar de peso, aumentar resistencia o mantenerse activo. Todo diseñado para tu nivel y ritmo.</p>
                    </div>
                </div>
            </div>
            <div className="col-12 col-sm-6 col-md-3 mb-5 px-3 div-card" >
                <div className="card h-100 border-0 card-box" >
                    <img src={imgUrl3} className="card-img-top" alt={'img-entrenamiento'} />
                    <div className="card-body d-flex flex-column align-items-center ">
                        <h5 className="card-title">Seguí todo tu Progreso</h5>
                        <p className="card-text text-center">Registrá tus sesiones completadas, observá tu evolución semana a semana y obtené estadísticas claras que te muestran tu mejora real.</p>
                    </div>
                </div>
            </div>
            <div className="col-12 col-sm-6 col-md-3 mb-5 px-3 div-card"> 
                <div className="card h-100 border-0 card-box" >
                    <img src={imgUrl2} className="card-img-top" alt={'img-entrenamiento'} />
                    <div className="card-body d-flex flex-column align-items-center ">
                        <h5 className="card-title">Gamificación y Motivación</h5>
                        <p className="card-text text-center">Desbloqueá logros, subí de nivel y alcanzá metas. Mantenerse motivado es clave para progresar, y FitPal te acompaña en cada paso.</p>
                    </div>
                </div>
            </div>
            <div className="col-12 col-sm-6 col-md-3 mb-5 px-3 div-card"> 
                <div className="card h-100 border-0 card-box">
                    <img src={imgUrl4} className="card-img-top" alt={'img-entrenamiento'} />
                    <div className="card-body d-flex flex-column align-items-center ">
                        <h5 className="card-title">Sesiones Claras y Guiadas</h5>
                        <p className="card-text text-center">Cada plan se divide en sesiones con ejercicios detallados: nombre, series, repeticiones y tiempo. Entrená sin dudas, con una estructura simple y directa.</p>
                    </div>
                </div>
            </div>                                                         
        </div>
    );
}

export default CardsInicio;