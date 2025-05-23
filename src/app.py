from flask import Flask, render_template, session, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from db import db
from routes.create import create_bp
from routes.verinformacion import verinformacion_bp
from routes.auth import auth_bp
from routes.actualizar import actualizar_bp
from routes.eliminar import eliminar_bp 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = '1234'

# Registro de blueprints
app.register_blueprint(create_bp, url_prefix='/crear')
app.register_blueprint(verinformacion_bp, url_prefix='/ver')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(actualizar_bp, url_prefix='/actualizar') 
app.register_blueprint(eliminar_bp, url_prefix='/eliminar') 

db.init_app(app)

@app.route('/')
def home():
    print("ola")
    return redirect(url_for('auth.login'))


@app.route('/ver/proveedores')
def bienvenida():
    if 'usuario' in session:
        return render_template('proveedores.html')  # Página de bienvenida
    else:
        return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
