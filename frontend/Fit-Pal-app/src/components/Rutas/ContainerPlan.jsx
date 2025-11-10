const ContainerPlan = ({imagen, titulo}) => {
    return (
        <div>
            <section className="hero2" style={{ background: `url(${imagen}) center/cover no-repeat` }}>

            </section>      
                <div className="container my-5 hero-div-2 d-flex flex-column justify-content-center align-items-center px-3">
                    <h1 className=" mb-4">{titulo}</h1>
                    <p>
                        En FitPal, cada usuario recibe un plan de entrenamiento diseñado de manera personalizada, 
                        teniendo en cuenta su nivel actual, sus objetivos y su disponibilidad de tiempo. 
                        Este enfoque permite que cada plan sea realmente útil y adecuado para la persona que lo va a llevar adelante, 
                        evitando rutinas genéricas que no se ajustan a sus necesidades reales.
                        <br />
                        La ruta de Planes de Entrenamiento es administrada por el usuario con rol Administrador, quien es responsable
                        de crear, asignar, modificar y gestionar los planes dentro del sistema. Cada plan está compuesto por:
                        <br />
                    </p>
                    <ul className="plan-info">
                        <li><strong>Objetivo del Plan:</strong> Define el propósito principal del plan, como ganar masa muscular, perder peso, mejorar resistencia, entre otros.</li>
                        <li><strong>Nivel de Dificultad:</strong> Clasifica el plan según la experiencia del usuario (principiante, intermedio, avanzado), asegurando que los ejercicios sean apropiados para su capacidad.</li>
                        <li><strong>Sesiones de Entrenamiento:</strong> Cada plan se divide en múltiples sesiones, que son unidades individuales de entrenamiento. Cada sesión incluye una serie de ejercicios específicos con detalles como nombre, series, repeticiones y tiempo de descanso.</li>
                    </ul>
                    <p>
                        Una vez asignado el plan al usuario, este puede visualizarlo desde su perfil y acceder
                        a cada una de las sesiones correspondientes. Al completar una sesión, el usuario puede
                        marcarla como realizada, lo que permite llevar un registro del progreso y fortalecer la
                        constancia del entrenamiento.
                        <br />
                        Gracias a esta estructura, FitPal se adapta tanto a quienes recién comienzan como a quienes
                        buscan mejorar rendimiento, aumentar masa muscular, bajar de peso o simplemente mantenerse activos.
                        <br />
                        El objetivo principal es garantizar que cada sesión tenga un propósito, que el usuario entienda
                        qué debe hacer y por qué, y que pueda ver sus avances a lo largo del tiempo, manteniéndose motivado
                        y acompañado en todo el proceso.
                    </p>
                </div>         
        </div>
    )
}

export default ContainerPlan;