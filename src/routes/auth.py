from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Usuario
from db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        user = Usuario.query.filter_by(Nombre=usuario).first()

        if user and user.Contraseña == contrasena:
            session['usuario'] = user.Nombre
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('bienvenida'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return render_template('index.html')

    return render_template('index.html')

@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('auth.login'))
