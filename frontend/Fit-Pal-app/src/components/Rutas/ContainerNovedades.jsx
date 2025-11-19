const ContainerNovedades = ({ imagen, titulo }) => {
    return (
        <div>
            <section className="hero2" style={{ background: `url(${imagen}) center/cover no-repeat` }}>

            </section>      
                <div className="container my-5 hero-div-2 d-flex flex-column justify-content-center align-items-center px-3">
                    <h1 className=" mb-4">{titulo}</h1>
                    <p>
                        En FitPal seguimos evolucionando para acompañarte mejor en tu entrenamiento.
                        <br />
                        En esta sección vas a encontrar las últimas actualizaciones, mejoras y nuevas 
                        funcionalidades de la plataforma.
                        <br />
                        Nuestro objetivo es brindarte una experiencia cada vez más clara, motivadora y personalizada.
                        Por eso, escuchamos a nuestra comunidad, analizamos el progreso de nuestros usuarios y trabajamos
                        continuamente en nuevas herramientas que te ayuden a mantener la constancia y ver resultados reales.
                        <br />
                    </p>
                    <ul className="plan-info">
                        <li><strong>Nuevas Funcionalidades:</strong> Descubrí las últimas incorporaciones a FitPal, desde nuevas métricas de seguimiento hasta opciones de personalización de planes.</li>
                        <li><strong>Mejoras en la Experiencia de Usuario:</strong> Trabajamos para que navegar por la plataforma sea más intuitivo y agradable, facilitando el acceso a tus planes y estadísticas.</li>
                        <li><strong>Consejos y Recursos:</strong> Compartimos artículos, videos y tips para maximizar tus entrenamientos y mantenerte motivado.</li>
                    </ul>
                    <p>
                        Te invitamos a explorar esta sección regularmente para estar al tanto de todas las novedades.
                        <br />
                        En FitPal, tu progreso es nuestra prioridad, y seguimos comprometidos en ofrecerte las mejores herramientas para que alcances tus objetivos de entrenamiento.
                    </p>
                </div>         
        </div>
    )
}

export default ContainerNovedades;