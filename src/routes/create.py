from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import db
from models import Remesa, Inventario, Proveedores, Ventas, Pagos, Paciente

# Definir el Blueprint para agregar información
create_bp = Blueprint('create', __name__, url_prefix='/crear')

# Ruta para agregar remesas
@create_bp.route('/agregar_remesa', methods=['GET', 'POST'])
def agregar_remesa():
    if request.method == 'POST':
        # Recuperar datos del formulario
        id_proveedor = request.form.get('Id_Proveedor')  # Proveedor seleccionado
        Código_Prod = request.form.get('Id_Producto')  # Producto seleccionado
        Modelo = request.form.get('modelo')
        Nombre = request.form.get('nombre')
        Num_Entradas = request.form.get('num_entradas')
        Factura = request.form.get('factura')
        Fecha = request.form.get('fecha')

        # Buscar el proveedor y producto en la base de datos usando sus IDs
        proveedor = Proveedores.query.get(id_proveedor)

        
        nueva_remesa = Remesa(
            Id_Proveedor=proveedor.Id_Proveedor,  # Relacionamos la remesa con el proveedor
            Código_Prod=Código_Prod,        # Relacionamos la remesa con el producto
            Modelo=Modelo,
            Nombre=Nombre,
            Num_Entradas=Num_Entradas,
            Factura=Factura,
            Fecha=Fecha
        )

            # Guardar la remesa en la base de datos
        db.session.add(nueva_remesa)
        db.session.commit()

        return redirect(url_for('verinformacion.ver_remesas'))  # Redirigir a la página de remesas

    # Obtener la lista de proveedores y productos para llenar los dropdowns
    proveedores = Proveedores.query.all()
    inventarios = Inventario.query.all()

    return render_template('crearinformacion/remesa.html', proveedores=proveedores, inventarios=inventarios)



# Ruta para agregar inventario
@create_bp.route('/agregar_inventario', methods=['GET', 'POST'])
def agregar_inventario():
    if request.method == 'POST':
        # Obtener datos del formulario
        Código_Prod = request.form['Código_Prod']
        Id_Proveedor = request.form['Id_Proveedor']
        Nombre_Prod = request.form['Nombre_Prod']
        Precio = request.form['Precio']
        Modelo = request.form['Modelo']
        Cantidad = request.form['Cantidad']
        Materiales = request.form['Materiales']

        # Crear una nueva instancia de Inventario
        nuevo_producto = Inventario(
            Código_Prod=Código_Prod,
            Id_Proveedor=Id_Proveedor,
            Nombre_Prod=Nombre_Prod,
            Precio=Precio,
            Modelo=Modelo,
            Cantidad=Cantidad,
            Materiales=Materiales
        )

        # Agregar el nuevo producto a la base de datos
        db.session.add(nuevo_producto)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir
        flash('Producto agregado con éxito', 'success')
        return redirect(url_for('create.agregar_inventario'))

    # Si el método es GET, obtener las listas de inventarios y proveedores para el formulario
    proveedores = Proveedores.query.all()  # Aquí consulta los proveedores desde el modelo Proveedores
    return render_template('crearinformacion/inventario.html', proveedores=proveedores)


# Ruta para agregar proveedor
@create_bp.route('/agregar_proveedor', methods=['GET', 'POST'])
def agregar_proveedor():
    if request.method == 'POST':
        # Obtener datos del formulario
        Id_Proveedor = request.form['Id_Proveedor']
        Nombre_Prov = request.form['Nombre_Prov']
        Correo = request.form['Correo']
        Dirección = request.form['Dirección']
        Teléfono = request.form['Teléfono']

        # Crear una nueva instancia de Proveedor
        nuevo_proveedor = Proveedores(
            Id_Proveedor=Id_Proveedor,
            Nombre_Prov=Nombre_Prov,
            Correo=Correo,
            Dirección=Dirección,
            Teléfono=Teléfono
        )

        # Agregar el nuevo proveedor a la base de datos
        db.session.add(nuevo_proveedor)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir
        flash('Proveedor agregado con éxito', 'success')
        return redirect(url_for('create.agregar_proveedor'))

    # Si el método es GET, mostrar el formulario para agregar proveedor
    return render_template('crearinformacion/proveedores.html')


# Ruta para agregar venta
@create_bp.route('/agregar_venta', methods=['GET', 'POST'])
def agregar_venta():
    if request.method == 'POST':
        # Obtener datos del formulario
        Id_Paciente = request.form['Id_Paciente']
        graduacion_ojo_derecho = request.form['graduacion_ojo_derecho']
        graduacion_ojo_izquierdo = request.form['graduacion_ojo_izquierdo']
        Armason = request.form['Armason']
        Tratamiento = request.form['Tratamiento']
        Anticipo = request.form['Anticipo']
        Adeudo = request.form['Adeudo']
        FechaVenta = request.form['FechaVenta']
        FechaEntrega = request.form['FechaEntrega']


        # Crear una nueva instancia de Venta
        nueva_venta = Ventas(
            Id_Paciente=Id_Paciente,
            graduacion_ojo_derecho=graduacion_ojo_derecho,
            graduacion_ojo_izquierdo=graduacion_ojo_izquierdo,
            Armason=Armason,
            Tratamiento=Tratamiento,
            Anticipo=Anticipo,
            Adeudo=Adeudo,
            FechaVenta=FechaVenta,
            FechaEntrega=FechaEntrega,
        )

        # Agregar la nueva venta a la base de datos
        db.session.add(nueva_venta)
        db.session.commit()

        flash('Venta agregada con éxito', 'success')
        return redirect(url_for('create.agregar_venta'))

    # Obtener la lista de pacientes desde la base de datos
    pacientes = db.session.query(Paciente).all()  
    inventarios = Inventario.query.all()
    
    invSerializado = [{"Nombre_Prod": i.Nombre_Prod, "Precio": i.Precio} for i in inventarios]
    
    return render_template('crearinformacion/ventas.html', pacientes=pacientes, inventarios=inventarios, invSerializado = invSerializado)



# Ruta para agregar pago
@create_bp.route('/agregar_pago', methods=['GET', 'POST'])
def agregar_pago():
    pacientes = Paciente.query.all()
    ventas = Ventas.query.all()
    ventas_json = [
        {
            "Id_Venta": v.Id_venta,
            "Id_Paciente": v.Id_Paciente,
            "Adeudo": float(v.Adeudo)
        }
        for v in ventas
    ]

    if request.method == 'POST':
        Id_Paciente = request.form['Id_Paciente']
        Id_Venta = request.form['Id_Venta']
        SaldoAPagar = float(request.form['SaldoAPagar'])
        Abono = float(request.form['Abono'])
        Fecha = request.form['Fecha']
        ProductoEntregado = 'ProductoEntregado' in request.form


        SaldoActual = SaldoAPagar - Abono
        if SaldoActual < 0:
            flash('Error: El abono no puede ser mayor al saldo a pagar.', 'danger')
            return redirect(url_for('create.agregar_pago'))

        nuevo_pago = Pagos(
            Id_Paciente=Id_Paciente,
            Id_Venta=Id_Venta,
            SaldoAPagar=SaldoAPagar,
            Abono=Abono,
            SaldoActual=SaldoActual,
            Fecha=Fecha,
            ProductoEntregado=ProductoEntregado
        )

        db.session.add(nuevo_pago)

        venta = Ventas.query.get(Id_Venta)
        if venta:
            venta.Adeudo = SaldoActual

        db.session.commit()
        flash('Pago agregado con éxito', 'success')
        return redirect(url_for('create.agregar_pago'))

    return render_template('crearinformacion/pagos.html', pacientes=pacientes, ventas=ventas, ventas_json=ventas_json)




# Ruta para agregar paciente
@create_bp.route('/agregar_paciente', methods=['GET', 'POST'])
def agregar_paciente():
    if request.method == 'POST':
        # Obtener datos del formulario
        Nombre_Pa = request.form['Nombre_Pa']
        Apellidos = request.form['Apellidos']
        Teléfono1 = request.form['Teléfono1']
        Teléfono2 = request.form['Teléfono2']
        Dirección = request.form['Dirección']
        Correo = request.form['Correo']

        # Crear una nueva instancia de Paciente
        nuevo_paciente = Paciente(
            Nombre_Pa=Nombre_Pa,
            Apellidos=Apellidos,
            Teléfono1=Teléfono1,
            Teléfono2=Teléfono2,
            Dirección=Dirección,
            Correo=Correo
        )

        # Agregar el nuevo paciente a la base de datos
        db.session.add(nuevo_paciente)
        db.session.commit()

        flash('Paciente agregado con éxito', 'success')
        return redirect(url_for('create.agregar_paciente'))

    return render_template('crearinformacion/pacientes.html')
