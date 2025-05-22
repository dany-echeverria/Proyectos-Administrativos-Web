from flask import Blueprint, jsonify
from db import db
from models import Proveedores, Inventario, Paciente, Remesa, Pagos, Ventas

eliminar_bp = Blueprint('eliminar', __name__)

@eliminar_bp.route('/borrar_proveedor/<int:id_proveedor>', methods=['DELETE'])
def borrar_proveedor(id_proveedor):
    proveedor = Proveedores.query.get(id_proveedor)
    if proveedor:
        db.session.delete(proveedor)
        db.session.commit()
        return jsonify({"success": True, "message": "Proveedor eliminado correctamente."})
    else:
        return jsonify({"success": False, "message": "Proveedor no encontrado."}), 404

@eliminar_bp.route('/borrar_producto/<int:id_producto>', methods=['DELETE'])
def borrar_producto(id_producto):
    producto = Inventario.query.get(id_producto)
    if producto:
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"success": True, "message": "Producto eliminado correctamente."})
    else:
        return jsonify({"success": False, "message": "Producto no encontrado."}), 404




# Ruta para borrar una remesa
@eliminar_bp.route('/borrar_remesa/<int:id_remesa>', methods=['DELETE'])
def borrar_remesa(id_remesa):
    remesa = Remesa.query.get(id_remesa)
    if remesa:
        db.session.delete(remesa)
        db.session.commit()
        return jsonify({"success": True, "message": "Remesa eliminada correctamente."})
    else:
        return jsonify({"success": False, "message": "Remesa no encontrada."}), 404
    



# Ruta para eliminar un pago
@eliminar_bp.route('/borrar_pago/<int:id_pago>', methods=['DELETE'])
def borrar_pago(id_pago):
    pago = Pagos.query.get(id_pago)
    if pago:
        db.session.delete(pago)
        db.session.commit()
        return jsonify({"success": True, "message": "Pago eliminado correctamente."})
    else:
        return jsonify({"success": False, "message": "Pago no encontrado."}), 404
    


@eliminar_bp.route('/borrar_venta/<int:id_venta>', methods=['DELETE'])
def borrar_venta(id_venta):
    print(f"Intentando eliminar venta con ID: {id_venta}")  # Para verificar si llega la solicitud
    venta = Ventas.query.get(id_venta)
    if venta:
        db.session.delete(venta)
        db.session.commit()
        print("Venta eliminada correctamente")  # Para confirmar que se eliminó
        return jsonify({"success": True, "message": "Venta eliminada correctamente."})
    else:
        print("Venta no encontrada")  # Si no encuentra el registro
        return jsonify({"success": False, "message": "Venta no encontrada."}), 404

    


#Pacoenteees
@eliminar_bp.route('/borrar_paciente/<int:id_paciente>', methods=['DELETE'])
def borrar_paciente(id_paciente):
    paciente = Paciente.query.get(id_paciente)
    if paciente:
        db.session.delete(paciente)
        db.session.commit()
        return jsonify({"success": True, "message": "Paciente eliminado correctamente."})
    else:
        return jsonify({"success": False, "message": "Paciente no encontrado."}), 404
