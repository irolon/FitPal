const CardExperiencias = () => {
    return (
        <div>
            <section className="container text-center py-5">
                <h2 className="fw-bold mb-4" style={{fontSize:'45px'}}>Lo que dicen nuestros usuarios</h2>

                <div className="row justify-content-center g-4 div-xp">
                    <div className="col-md-4">
                    <p className="fst-italic" style={{fontSize:'20px'}}>"Me ayudó a mantener la constancia. Las sesiones son claras y fáciles de seguir."</p>
                    <p style={{fontSize:'18px', marginTop:'30px'}}><strong>- Lucas</strong></p>
                    </div>
                    <div className="col-md-4">
                    <p className="fst-italic" style={{fontSize:'20px'}}>"Volví a entrenar después de años. Ver mi progreso me motivó una banda."</p>
                    <p style={{fontSize:'18px', marginTop:'30px'}}><strong>- Andrea</strong></p>
                    </div>
                    <div className="col-md-4">
                    <p className="fst-italic" style={{fontSize:'20px'}}>"Los planes se adaptan a mi tiempo. Eso hizo toda la diferencia."</p>
                    <p style={{fontSize:'18px', marginTop:'30px'}}><strong>- Sofía</strong></p>
                    </div>
                </div>
            </section>             
        </div>
    )
}

export default CardExperiencias;