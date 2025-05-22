from flask import Blueprint, render_template
from models import Inventario

productos_bp = Blueprint("productos", __name__)

# Endpoint para listar productos
@productos_bp.route('/productos')
def lista_productos():
    productos = Inventario.query.all()  # Obtener todos los productos de la base de datos
    return render_template('productos/lista_productos.html', productos=productos)
