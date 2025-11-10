import {BiUserCheck, BiClipboard, BiDumbbell} from 'react-icons/bi';

const CardFuncionamiento = () => {
    return (
    <section className="container my-5">
        <h2 className="text-center m-5" style={{fontSize:'45px',fontWeight:'bold'}}>¿Cómo funciona?</h2>
        <div className="row g-4 my-5 ">
            <div className="col-12 col-md-4">
                <div className="p-4 border rounded-4 h-100 text-center">
                    <BiUserCheck className="display-6 mb-3" size={66}/>
                    <h2 className='m-5' style={{fontSize:'30px',fontWeight:'bold'}}>Creá tu perfil</h2>
                    <p  style={{fontSize:'20px'}}>Definí objetivos, nivel y disponibilidad. Listo para empezar.</p>
                </div>
            </div>
            <div className="col-12 col-md-4">
                <div className="p-4 border rounded-4 h-100 text-center">
                    <BiClipboard className="display-6 mb-3" size={64}/>
                    <h2 className='m-5' style={{fontSize:'30px',fontWeight:'bold'}}>Recibí tu plan</h2>
                    <p  style={{fontSize:'20px'}}>Rutinas personalizadas con sesiones claras y guiadas.</p>
                </div>
            </div>
            <div className="col-12 col-md-4">
                <div className="p-4 border rounded-4 h-100 text-center">
                    <BiDumbbell className="display-6 mb-3" size={64}/>
                    <h2 className='m-5' style={{fontSize:'30px',fontWeight:'bold'}}>Entrená</h2>
                    <p style={{fontSize:'20px'}}>Marcá sesiones, sumá puntos y seguí tu progreso.</p>
                </div>
            </div>
        </div>
    </section>
    );
}

export default CardFuncionamiento;