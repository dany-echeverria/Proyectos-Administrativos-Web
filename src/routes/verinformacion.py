from flask import Blueprint, render_template, request
from models import Remesa, Inventario, Proveedores, Ventas, Paciente, Pagos
from sqlalchemy.orm import joinedload


verinformacion_bp = Blueprint('verinformacion', __name__)

# Función genérica para paginación
def get_paginated_query(query, page, per_page=5):
    return query.paginate(page=page, per_page=per_page, error_out=False)

@verinformacion_bp.route('/inventarios', methods=['GET'])
def ver_inventarios():
    page = request.args.get('page', 1, type=int)
    campo = request.args.get('campo')
    valor = request.args.get('valor')

    query = Inventario.query

    if campo and valor:
        if campo == 'Nombre_Prod':
            query = query.filter(Inventario.Nombre_Prod.ilike(f"%{valor}%"))
        elif campo == 'Modelo':
            query = query.filter(Inventario.Modelo.ilike(f"%{valor}%"))
        elif campo == 'Materiales':
            query = query.filter(Inventario.Materiales.ilike(f"%{valor}%"))
        elif campo == 'Id_Proveedor':
            try:
                query = query.filter(Inventario.Id_Proveedor == int(valor))
            except ValueError:
                query = query.filter(False)  # evita errores si no es entero

    paginated = query.paginate(page=page, per_page=5, error_out=False)

    return render_template(
        'verinformacion/inventarios.html',
        datos=paginated.items,
        page=page,
        total_pages=paginated.pages
    )
@verinformacion_bp.route('/proveedores', methods=['GET'])
def ver_proveedores():
    page = request.args.get('page', 1, type=int)
    campo = request.args.get('campo')
    valor = request.args.get('valor')
    query = Proveedores.query

    if campo and valor:
        if campo == 'Nombre_Prov':
            query = query.filter(Proveedores.Nombre_Prov.ilike(f"%{valor}%"))
        elif campo == 'Correo':
            query = query.filter(Proveedores.Correo.ilike(f"%{valor}%"))
        elif campo == 'Dirección':
            query = query.filter(Proveedores.Dirección.ilike(f"%{valor}%"))
        elif campo == 'Teléfono':
            query = query.filter(Proveedores.Teléfono.ilike(f"%{valor}%"))

    paginated = get_paginated_query(query, page)
    return render_template('verinformacion/proveedores.html', datos=paginated.items, page=page, total_pages=paginated.pages)

@verinformacion_bp.route('/remesas', methods=['GET'])
def ver_remesas():
    page = request.args.get('page', 1, type=int)
    campo = request.args.get('campo')
    valor = request.args.get('valor')
    query = Remesa.query

    if campo and valor:
        if campo == 'proveedor':
            query = query.filter(Remesa.Id_Proveedor.ilike(f"%{valor}%"))
        elif campo == 'Modelo':
            query = query.filter(Remesa.Modelo.ilike(f"%{valor}%"))
        elif campo == 'Nombre':
            query = query.filter(Remesa.Nombre.ilike(f"%{valor}%"))
        elif campo == 'Factura':
            query = query.filter(Remesa.Factura.ilike(f"%{valor}%"))

    paginated = get_paginated_query(query, page)
    return render_template('verinformacion/remesa.html', datos=paginated.items, page=page, total_pages=paginated.pages)

@verinformacion_bp.route('/ventas', methods=['GET'])
def ver_ventas():
    page = request.args.get('page', 1, type=int)
    campo = request.args.get('campo')
    valor = request.args.get('valor')
    query = Ventas.query

    if campo and valor:
        if campo == 'Armason':
            query = query.filter(Ventas.Armason.ilike(f"%{valor}%"))
        elif campo == 'Tratamiento':
            query = query.filter(Ventas.Tratamiento.ilike(f"%{valor}%"))
        elif campo == 'Id_Paciente':
            query = query.filter(Ventas.Id_Paciente.ilike(f"%{valor}%"))
        elif campo == 'Id_venta':
            query = query.filter(Ventas.Id_venta.ilike(f"%{valor}%"))
        elif campo == 'FechaEntrega':
            query = query.filter(Ventas.FechaEntrega.ilike(f"%{valor}%"))
        elif campo == 'FechaVenta':
            query = query.filter(Ventas.FechaVenta.ilike(f"%{valor}%"))


    paginated = get_paginated_query(query, page)
    return render_template('verinformacion/ventas.html', datos=paginated.items, page=page, total_pages=paginated.pages)

@verinformacion_bp.route('/pacientes', methods=['GET'])
def ver_pacientes():
    page = request.args.get('page', 1, type=int)
    campo = request.args.get('campo')
    valor = request.args.get('valor')
    query = Paciente.query

    if campo and valor:
        if campo == 'Nombre_Pa':
            query = query.filter(Paciente.Nombre_Pa.ilike(f"%{valor}%"))
        elif campo == 'Apellidos':
            query = query.filter(Paciente.Apellidos.ilike(f"%{valor}%"))
        elif campo == 'Correo':
            query = query.filter(Paciente.Correo.ilike(f"%{valor}%"))

    paginated = get_paginated_query(query, page)
    return render_template('verinformacion/paciente.html', datos=paginated.items, page=page, total_pages=paginated.pages)

@verinformacion_bp.route('/pagos', methods=['GET'])
def ver_pagos():
    page = request.args.get('page', 1, type=int)
    campo = request.args.get('campo')
    valor = request.args.get('valor')
    query = Pagos.query

    if campo and valor:
        if campo == 'SaldoAPagar':
            try:
                query = query.filter(Pagos.SaldoAPagar == float(valor))
            except:
                query = query.filter(False)
        elif campo == 'Abono':
            try:
                query = query.filter(Pagos.Abono == float(valor))
            except:
                query = query.filter(False)
        elif campo == 'Id_Paciente':
            query = query.filter(Pagos.Id_Paciente.ilike(f"%{valor}%"))
        elif campo == 'Id_Pago':
            query = query.filter(Pagos.Id_Pago.ilike(f"%{valor}%"))
        elif campo == 'Id_Venta':
            query = query.filter(Pagos.Id_Venta.ilike(f"%{valor}%"))
        elif campo == 'Fecha':
            query = query.filter(Pagos.Fecha.ilike(f"%{valor}%"))

    paginated = get_paginated_query(query, page)
    return render_template('verinformacion/pagos.html', datos=paginated.items, page=page, total_pages=paginated.pages)