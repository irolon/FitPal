const CardComenzar = () => {
    return (
        <div>
            <section className="text-center py-5 comenzar" style={{ backgroundColor: '#111', color: 'white' }}>
                <h2 className="fw-bold mb-3">¿Listo para empezar?</h2>
                <p className="mb-4" style={{ maxWidth: '600px', margin: 'auto' }}>
                    Unite a FitPal y comenzá tu camino hacia una mejor versión de vos mismo.
                    Entrenamientos claros, progreso visible y motivación constante.
                </p>
                <a href="#" className="btn btn-light btn-lg rounded-pill px-4 py-2">
                    Crear mi cuenta
                </a>
            </section>


        </div>

    )
}

export default CardComenzar;