from flask import Flask
from flask_cors import CORS


# --------------------------
# Rutas FitPal
# --------------------------
from routes.ejercicio_routes import ejercicios_bp
from routes.login_routes import login_bp
from routes.register_routes import register_bp
from routes.Plan_entrenamiento import plan_entrenamiento_bp
from routes.plan_sesion_routes import plan_sesion_bp
from routes.ejercicio_routes import ejercicios_bp
from routes.sesion_routes import sesiones_bp
from routes.progreso_ejercicio_routes import progreso_ejercicio_bp
from routes.administrador_routes import administrador_bp


# --------------------------
# Configuración Flask
# --------------------------
app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:5174",
            "http://127.0.0.1:5174"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})


# --------------------------
# Registro de Rutas / Blueprints
# --------------------------

app.register_blueprint(login_bp, url_prefix="/api")
app.register_blueprint(register_bp, url_prefix="/api")
app.register_blueprint(plan_entrenamiento_bp, url_prefix="/api")
app.register_blueprint(plan_sesion_bp)
app.register_blueprint(ejercicios_bp, url_prefix="/api")
app.register_blueprint(sesiones_bp, url_prefix="/api/admin")
app.register_blueprint(progreso_ejercicio_bp, url_prefix="/api")
app.register_blueprint(administrador_bp, url_prefix="/api")

# --------------------------
# Main
# --------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
