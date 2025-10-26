from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey,
    DateTime, Date, Numeric, Text
)
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base


# --- MARCA ---
class Marca(Base):
    __tablename__ = "marcas"
    id_marca = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

    usuarios = relationship("Usuario", back_populates="marca_obj")
    leads = relationship("Lead", back_populates="marca_obj")
    productos = relationship("Producto", back_populates="marca_obj")

# --- ESTADO ---
class Estado(Base):
    __tablename__ = "estados"
    id_estado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(Text)

    leads = relationship("Lead", back_populates="estado_obj")

# --- TIPO CLIENTE ---
class TipoCliente(Base):
    __tablename__ = "tipo_cliente"
    id_tipo_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    leads = relationship("Lead", back_populates="tipo_cliente_obj")

# --- CATEGORIA ---
class Categoria(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    # descripcion = Column(Text)

    leads = relationship("Lead", back_populates="categoria_obj")

# --- COMUNA ---
class Comuna(Base):
    __tablename__ = "comunas"
    id_comuna      = Column(Integer, primary_key=True, index=True)
    nombre         = Column(String(100), unique=True, nullable=False)
    # costo_despacho = Column(Numeric(12, 2), nullable=False, default=0)

    leads = relationship("Lead", back_populates="comuna_obj")

# --- USUARIO ---
class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario      = Column(Integer, primary_key=True, index=True)
    nombre_usuario  = Column(String(100), nullable=False)
    email           = Column(String(150), unique=True, nullable=False)
    password_hash   = Column(String, nullable=False)
    nivel           = Column(String(20), nullable=False)
    status          = Column(Boolean, default=True)
    id_marca        = Column(Integer, ForeignKey("marcas.id_marca"))

    marca_obj       = relationship("Marca", back_populates="usuarios")
    usuario_marcas  = relationship("UsuarioMarcas", back_populates="usuario")
    leads           = relationship("Lead", back_populates="usuario_obj")

# --- USUARIO-MARCAS (muchos a muchos marcas por usuario) ---
class UsuarioMarcas(Base):
    __tablename__ = "usuario_marcas"
    id_usuario  = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    id_marca    = Column(Integer, ForeignKey("marcas.id_marca"),   primary_key=True)

    usuario     = relationship("Usuario", back_populates="usuario_marcas")
    marca       = relationship("Marca")

# --- LEAD ---
class Lead(Base):
    __tablename__ = "leads"
    id_lead         = Column(Integer, primary_key=True, index=True)
    codigo_cliente  = Column(String(50), nullable=False, unique=True)
    fecha_ingreso = Column(Date, default=datetime.now().date)
    id_marca        = Column(Integer, ForeignKey("marcas.id_marca"), nullable=False)
    nombre_cliente  = Column(String(150), nullable=False)
    id_categoria    = Column(Integer, ForeignKey("categorias.id_categoria"))
    id_tipo_cliente = Column(Integer, ForeignKey("tipo_cliente.id_tipo_cliente"))
    plataforma      = Column(String(50))
    fecha_evento    = Column(Date)
    dia             = Column(String(20))
    mes             = Column(String(20))
    semana          = Column(Integer)
    anio            = Column(Integer)
    id_comuna       = Column(Integer, ForeignKey("comunas.id_comuna"))
    telefono        = Column(String(20))
    whatsapp_link   = Column(Text)
    email           = Column(String(150))
    monto_cotizado  = Column(Numeric(12, 2), default=0)
    id_estado       = Column(Integer, ForeignKey("estados.id_estado"))
    fecha_cierre    = Column(Date)
    seguimiento     = Column(Text)
    fecha_seguimiento = Column(Date)
    id_usuario      = Column(Integer, ForeignKey("usuarios.id_usuario"))
    numero_cotizacion = Column(String(50))
    segmentacion    = Column(String(30))
    created_at      = Column(DateTime, default=datetime.utcnow)
    updated_at      = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creado_por      = Column(String(100))

    marca_obj       = relationship("Marca", back_populates="leads")
    categoria_obj   = relationship("Categoria", back_populates="leads")
    tipo_cliente_obj= relationship("TipoCliente", back_populates="leads")
    comuna_obj      = relationship("Comuna", back_populates="leads")
    estado_obj      = relationship("Estado", back_populates="leads")
    usuario_obj     = relationship("Usuario", back_populates="leads")
    cotizaciones    = relationship("Cotizacion", back_populates="lead")

# --- PRODUCTO ---
class Producto(Base):
    __tablename__ = "productos"
    id_producto     = Column(Integer, primary_key=True, index=True)
    id_marca        = Column(Integer, ForeignKey("marcas.id_marca"), nullable=False)
    nombre_producto = Column(Text, nullable=False)
    descripcion     = Column(Text)
    costo           = Column(Numeric(12, 2), nullable=False, default=0)
    precio_sugerido = Column(Numeric(12, 2), nullable=False, default=0)
    activo          = Column(Boolean, nullable=False, default=True)
    creado_at       = Column(DateTime, default=datetime.utcnow)

    marca_obj       = relationship("Marca", back_populates="productos")
    lineas          = relationship("CotizacionProducto", back_populates="producto")

# --- COTIZACION ---
class Cotizacion(Base):
    __tablename__ = "cotizaciones"
    id_cotizacion   = Column(Integer, primary_key=True, index=True)
    id_lead         = Column(Integer, ForeignKey("leads.id_lead"), nullable=False)
    id_usuario      = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)
    nro_version     = Column(Integer, nullable=False, default=1)
    subtotal        = Column(Numeric(12, 2), nullable=False, default=0)
    iva             = Column(Numeric(12, 2), nullable=False, default=0)
    traslado        = Column(Numeric(12, 2), nullable=False, default=0)
    extras          = Column(Numeric(12, 2), nullable=False, default=0)
    descuento       = Column(Numeric(12, 2), nullable=False, default=0)
    descuento_tipo  = Column(String(10), default="monto")  # monto | porcentaje
    total           = Column(Numeric(12, 2), nullable=False, default=0)
    fecha_creacion  = Column(DateTime, default=datetime.utcnow)
    leyenda_iva     = Column(String(200))
    estado          = Column(String(30), default="Generada")
    pdf_url         = Column(String(255))
    notas           = Column(Text)

    lead            = relationship("Lead", back_populates="cotizaciones")
    usuario         = relationship("Usuario")
    items           = relationship("CotizacionProducto", back_populates="cotizacion")

# --- COTIZACION-PRODUCTO ---
class CotizacionProducto(Base):
    __tablename__ = "cotizacion_productos"
    id                = Column(Integer, primary_key=True, index=True)
    id_cotizacion     = Column(Integer, ForeignKey("cotizaciones.id_cotizacion"), nullable=False)
    id_producto       = Column(Integer, ForeignKey("productos.id_producto"), nullable=False)
    cantidad          = Column(Integer, nullable=False)
    precio_unitario   = Column(Numeric(12, 2), nullable=False)
    total_linea       = Column(Numeric(12, 2), nullable=False)

    cotizacion        = relationship("Cotizacion", back_populates="items")
    producto          = relationship("Producto", back_populates="lineas")

# --- SEGMENTACION ---
class Segmentacion(Base):
    __tablename__ = "segmentacion"
    id_segmentacion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), nullable=False, unique=True)
