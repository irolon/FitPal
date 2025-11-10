
const ContainerNosotros = ({imagen, titulo}) => {
    return (
        <div>
            <section className="hero2" style={{ background: `url(${imagen}) center/cover no-repeat` }}>

            </section>      
                <div className="container my-5 hero-div-2 d-flex flex-column justify-content-center align-items-center px-3">
                    <h1 className=" mb-4">{titulo}</h1>
                    <p>FitPal nació con una idea simple: hacer que entrenar sea más accesible, claro y motivador para todos.
                        Muchas personas comienzan el gimnasio llenos de ganas, pero se encuentran con un problema común: no saber exactamente qué hacer, cómo estructurar sus entrenamientos o cómo medir su progreso. Esa falta de claridad lleva a frustración, desmotivación y abandono.
                        <br />
                        Observamos esto de cerca —en amigos, familiares e incluso en nosotros mismos— y entendimos que la clave no estaba en “entrenar más”, sino en entrenar mejor, con propósito.
                        <br />                    
                        Por eso creamos FitPal: un entrenador digital que acompaña, guía y motiva.
                        <br />
                        La aplicación te ofrece planes personalizados según tus objetivos y tu nivel, divide los entrenamientos en sesiones claras y te permite seguir tu progreso paso a paso. Cada sesión completada, cada avance, cada logro se convierte en una parte visible de tu crecimiento.
                        <br />
                        Pero FitPal no solo sirve para entrenar: también construye constancia.
                        Porque creemos que el verdadero cambio se logra todos los días, con pequeños pasos sostenidos en el tiempo.
                        <br />
                        FitPal es para quienes recién empiezan, para quienes vuelven después de un tiempo, para quienes buscan progreso, para quienes quieren desafiarse y superar sus propios límites.
                        <br />
                        No importa tu punto de partida.
                        Lo importante es seguir avanzando.
                        <br />
                        FitPal está acá para acompañarte en el camino.
                        </p>
                </div>         
        </div>
    )
}

export default ContainerNosotros;