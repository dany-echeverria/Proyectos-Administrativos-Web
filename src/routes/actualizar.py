from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Inventario, Paciente, Pagos, Proveedores, Ventas, Remesa

actualizar_bp = Blueprint("actualizar", __name__)

@actualizar_bp.route("/editar_producto/<int:codigo>", methods=["GET", "POST"])
def editar_producto(codigo):
    producto = Inventario.query.get_or_404(codigo)

    if request.method == "POST":
        # Obtener los nuevos datos del formulario
        producto.Id_Proveedor = request.form["Id_Proveedor"]
        producto.Nombre_Prod = request.form["Nombre_Prod"]
        producto.Precio = request.form["Precio"]
        producto.Modelo = request.form["Modelo"]
        producto.Cantidad = request.form["Cantidad"]
        producto.Materiales = request.form["Materiales"]

        db.session.commit()  # Guardar cambios en la BD
        return redirect(url_for("verinformacion.ver_inventarios"))  # Redirige al listado de productos

    return render_template("actualizarinformacion/inventario.html", producto=producto)


@actualizar_bp.route("/editar_paciente/<int:codigo>", methods=["GET", "POST"])
def editar_paciente(codigo):
    paciente = Paciente.query.get_or_404(codigo)  # Buscar por Id_Paciente

    if request.method == "POST":
        # Obtener los nuevos datos del formulario
        paciente.Nombre_Pa = request.form["Nombre_Pa"]
        paciente.Apellidos = request.form["Apellidos"]
        paciente.Teléfono1 = request.form["Teléfono1"]
        paciente.Teléfono2 = request.form["Teléfono2"]
        paciente.Dirección = request.form["Dirección"]
        paciente.Correo = request.form["Correo"]

        db.session.commit()  # Guardar cambios en la BD
        return redirect(url_for("verinformacion.ver_pacientes"))  # Redirige al listado de pacientes

    return render_template("actualizarinformacion/paciente.html", paciente=paciente)


@actualizar_bp.route("/editar_pago/<int:pago_id>", methods=["GET", "POST"])
def editar_pago(pago_id):
    pago = Pagos.query.get_or_404(pago_id)

    if request.method == "POST":
        pago.Id_Paciente = request.form["Id_Paciente"]
        pago.Id_Venta = request.form["Id_Venta"]
        pago.SaldoAPagar = request.form["SaldoAPagar"]
        pago.Abono = request.form["Abono"]
        pago.SaldoActual = request.form["SaldoActual"]
        pago.Fecha = request.form["Fecha"]

        db.session.commit()
        return redirect(url_for("verinformacion.ver_pagos"))

    return render_template("actualizarinformacion/pagos.html", pago=pago)



@actualizar_bp.route("/editar_proveedor/<int:id>", methods=["GET", "POST"])
def actualizar_proveedor(id):
    proveedor = Proveedores.query.get_or_404(id)

    if not proveedor:
        return "Proveedor no encontrado", 404

    if request.method == "POST":
        proveedor.Nombre_Prov = request.form["nombre"]
        proveedor.Correo = request.form["correo"]
        proveedor.Dirección = request.form["direccion"]
        proveedor.Teléfono = request.form["telefono"]
        proveedor.Código_Prod = request.form["producto"]

        db.session.commit()
        return redirect(url_for("verinformacion.ver_proveedores"))

    return render_template("actualizarinformacion/proveedores.html", proveedor=proveedor)




@actualizar_bp.route("/editar_venta/<int:id>", methods=["GET", "POST"])
def editar_venta(id):
    venta = Ventas.query.get_or_404(id)

    if not venta:
        return "Proveedor no encontrado", 404

    if request.method == "POST":
        venta.Id_venta = request.form["Id_venta"]
        venta.Id_Paciente = request.form["Id_Paciente"]
        venta.graduacion_ojo_derecho = request.form["graduacion_ojo_derecho"]
        venta.graduacion_ojo_izquierdo = request.form["graduacion_ojo_izquierdo"]
        venta.Armason = request.form["Armason"]
        venta.Tratamiento = request.form["Tratamiento"]
        venta.Anticipo = request.form["Anticipo"]
        venta.Adeudo = request.form["Adeudo"]
        venta.Fecha = request.form["Fecha"]

        db.session.commit()
        return redirect(url_for("verinformacion.ver_ventas"))

    return render_template("actualizarinformacion/ventas.html", venta=venta)






@actualizar_bp.route("/editar_remesa/<int:id>", methods=["GET", "POST"])
def editar_remesa(id):
    remesa = Remesa.query.get_or_404(id)

    if not remesa:
        return "Remesa no encontrado", 404

    if request.method == "POST":
        remesa.id = request.form["id"]
        remesa.Proveedor = request.form["Proveedor"]
        remesa.CodigoElemento = request.form["CodigoElemento"]
        remesa.Modelo = request.form["Modelo"]
        remesa.Nombre = request.form["Nombre"]
        remesa.Num_Entradas = request.form["Num_Entradas"]
        remesa.Factura = request.form["Factura"]
        remesa.Fecha = request.form["Fecha"]

        db.session.commit()
        return redirect(url_for("verinformacion.ver_remesas"))

    return render_template("actualizarinformacion/remesa.html", remesa=remesa)
