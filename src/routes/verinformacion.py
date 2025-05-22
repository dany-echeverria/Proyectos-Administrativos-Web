from flask import Blueprint, render_template, request
from models import Remesa, Inventario, Proveedores, Ventas, Paciente, Pagos

verinformacion_bp = Blueprint('verinformacion', __name__)

# Función genérica para paginación
def get_paginated_query(query, page, per_page=5):
    return query.paginate(page=page, per_page=per_page, error_out=False)

@verinformacion_bp.route('/inventarios', methods=['GET'])
def ver_inventarios():
    page = request.args.get('page', 1, type=int)  # Obtener número de página (por defecto 1)
    
    inventarios_paginated = get_paginated_query(Inventario.query, page)

    return render_template(
        'verinformacion/inventarios.html', 
        datos=inventarios_paginated.items,  # Registros de la página actual
        page=page,
        total_pages=inventarios_paginated.pages
    )

@verinformacion_bp.route('/proveedores', methods=['GET'])
def ver_proveedores():
    page = request.args.get('page', 1, type=int)

    proveedores_paginated = get_paginated_query(Proveedores.query, page)

    return render_template(
        'verinformacion/proveedores.html', 
        datos=proveedores_paginated.items,
        page=page,
        total_pages=proveedores_paginated.pages
    )

@verinformacion_bp.route('/remesas', methods=['GET'])
def ver_remesas():
    page = request.args.get('page', 1, type=int)

    remesas_paginated = get_paginated_query(Remesa.query, page)

    return render_template(
        'verinformacion/remesa.html', 
        datos=remesas_paginated.items,
        page=page,
        total_pages=remesas_paginated.pages
    )

@verinformacion_bp.route('/ventas', methods=['GET'])
def ver_ventas():
    page = request.args.get('page', 1, type=int)

    ventas_paginated = get_paginated_query(Ventas.query, page)

    return render_template(
        'verinformacion/ventas.html', 
        datos=ventas_paginated.items,
        page=page,
        total_pages=ventas_paginated.pages
    )

@verinformacion_bp.route('/pacientes', methods=['GET'])
def ver_pacientes():
    page = request.args.get('page', 1, type=int)

    pacientes_paginated = get_paginated_query(Paciente.query, page)

    return render_template(
        'verinformacion/paciente.html', 
        datos=pacientes_paginated.items,
        page=page,
        total_pages=pacientes_paginated.pages
    )

@verinformacion_bp.route('/pagos', methods=['GET'])
def ver_pagos():
    page = request.args.get('page', 1, type=int)
    pacientes = Paciente.query.all()
    pagos_paginated = get_paginated_query(Pagos.query, page)

    return render_template(
        'verinformacion/pagos.html', 
        datos=pagos_paginated.items,
        page=page,
        total_pages=pagos_paginated.pages,
        pacientes = pacientes
    )
