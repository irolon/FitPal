import CardImgCenter from "../Cards/CardImgCenter";
import CardsInicio from "../Cards/CardsInicio";
import ItemListContainer from "../Inicio/ItemListContainer";
import CardFuncionamiento from "../Cards/CardFuncionamiento";
import CardComenzar from "../Cards/CardComenzar";
import CardExperiencias from "../Cards/CardExperiencias";


const HomeListContainer = () => {
    return (
        <div>
            <ItemListContainer  titulo={'¿Qué es FitPal?'} subtitulo={'FitPal es tu entrenador digital personalizado. Recibí planes de entrenamiento, seguí tu progreso y mantenete motivado con logros y niveles.'}/>
            <div className="container my-5">

                <div className="row">
                    <div className="col">
                    <h2 className="text-center mb-5 titulo-cards">Tu entrenamiento empieza acá</h2>
                    </div>
                </div>
                <CardsInicio />
            </div>
            <CardImgCenter />
            <CardFuncionamiento />
            <CardComenzar />
            <CardExperiencias />
        </div>

    );
}

export default HomeListContainer;