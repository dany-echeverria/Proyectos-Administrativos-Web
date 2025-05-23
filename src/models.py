from db import db

# Modelo de Inventario
# Clase Remesa
class Remesa(db.Model):
    __tablename__ = 'remesa'
    Id_Remesa = db.Column(db.Integer, primary_key=True)
    Id_Proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.Id_Proveedor'), nullable=False)
    Código_Prod =  db.Column(db.Integer, db.ForeignKey('inventario.Código_Prod'), nullable=False)
    Modelo = db.Column(db.String(50), nullable=False)
    Nombre = db.Column(db.String(100), nullable=False)
    Num_Entradas = db.Column(db.Integer, nullable=False)
    Factura = db.Column(db.String(100), nullable=False)
    Fecha = db.Column(db.Date, nullable=False)

    proveedor = db.relationship('Proveedores', backref='remesas')
    producto = db.relationship('Inventario', backref='remesas')


# Clase Inventario
class Inventario(db.Model):
    __tablename__ = 'inventario'
    __table_args__ = {'extend_existing': True}
    
    Código_Prod = db.Column(db.Integer, primary_key=True)
    Id_Proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.Id_Proveedor'))
    Nombre_Prod = db.Column(db.Text)
    Precio = db.Column(db.Numeric(10, 2))
    Modelo = db.Column(db.Text)
    Cantidad = db.Column(db.Integer)
    Materiales = db.Column(db.Text)

    proveedor = db.relationship('Proveedores', backref='productos')



# Modelo de Proveedores
class Proveedores(db.Model):
    __tablename__ = 'proveedores'
    
    Id_Proveedor = db.Column(db.Integer, primary_key=True)
    Nombre_Prov = db.Column(db.Text)
    Correo = db.Column(db.Text)
    Dirección = db.Column(db.Text)
    Teléfono = db.Column(db.Text)


# Una tabla intermedia para manejar la relación muchos a muchos entre Remesas y Productos
# Modelo de Ventas
class Ventas(db.Model):
    __tablename__ = 'ventas'
    Id_venta = db.Column(db.Integer, primary_key=True)
    Id_Paciente = db.Column(db.Integer, db.ForeignKey('paciente.Id_Paciente'))
    paciente = db.relationship('Paciente', backref='ventas')
    
    graduacion_ojo_derecho = db.Column(db.String(100))
    graduacion_ojo_izquierdo = db.Column(db.String(100))
    Armason = db.Column(db.Text)
    Tratamiento = db.Column(db.Text)
    Anticipo = db.Column(db.Numeric(10, 2))
    Adeudo = db.Column(db.Numeric(10, 2))
    FechaVenta = db.Column(db.Date)
    FechaEntrega = db.Column(db.Date)
    observaciones = db.Column(db.Text)

# Modelo de Paciente
class Paciente(db.Model):
    __tablename__ = 'paciente'
    Id_Paciente = db.Column(db.Integer, primary_key=True)
    Nombre_Pa = db.Column(db.Text)
    Apellidos = db.Column(db.Text)
    Teléfono1 = db.Column(db.Text)
    Teléfono2 = db.Column(db.Text)
    Dirección = db.Column(db.Text)
    Correo = db.Column(db.Text)

# Modelo de Pagos
class Pagos(db.Model):
    __tablename__ = 'pagos'
    Id_Pago = db.Column(db.Integer, primary_key=True)
    Id_Paciente = db.Column(db.Integer, db.ForeignKey('paciente.Id_Paciente'))
    paciente = db.relationship('Paciente', backref='pagos')
    
    Id_Venta = db.Column(db.Integer, db.ForeignKey('ventas.Id_venta'))
    venta = db.relationship('Ventas', backref='pagos')
    
    SaldoAPagar = db.Column(db.Numeric(10, 2))
    Abono = db.Column(db.Numeric(10, 2))
    SaldoActual = db.Column(db.Numeric(10, 2))
    Fecha = db.Column(db.Date)
    ProductoEntregado = db.Column(db.Boolean, default=False)

# Modelo de Usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    Id_Usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.Text)
    Contraseña = db.Column(db.Text)
