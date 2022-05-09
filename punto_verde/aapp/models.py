# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    id_venta = models.OneToOneField('Compra', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre = models.CharField(max_length=100)
    forma_pago = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'boleta'


class Compra(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    monto = models.IntegerField()
    forma_pago = models.CharField(max_length=10)
    fecha_venta = models.DateField()
    reserva_id_reserva = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva')
    retiro_id_retiro = models.ForeignKey('Retiro', models.DO_NOTHING, db_column='retiro_id_retiro')
    emitido_en = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'compra'


class Comprador(models.Model):
    id_comprador = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'comprador'


class ContenedorLleno(models.Model):
    id_lleno = models.IntegerField(primary_key=True)
    reservado = models.CharField(max_length=1)
    lleno = models.CharField(max_length=1)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva', blank=True, null=True)
    llen_conts_id_llenado = models.OneToOneField('LlenadoContenedores', models.DO_NOTHING, db_column='llen_conts_id_llenado')
    precios_id_precio = models.ForeignKey('Precios', models.DO_NOTHING, db_column='precios_id_precio')

    class Meta:
        managed = False
        db_table = 'contenedor_lleno'


class DetaAsignacion(models.Model):
    contenedor_id_contenedor = models.ForeignKey('LlenadoContenedores', models.DO_NOTHING, db_column='contenedor_id_contenedor')
    receptor_rut_receptor = models.ForeignKey('Receptor', models.DO_NOTHING, db_column='receptor_rut_receptor')

    class Meta:
        managed = False
        db_table = 'deta_asignacion'


class Empleado(models.Model):
    rut_empleado = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.IntegerField()
    ocupacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    id_venta = models.OneToOneField(Compra, models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    giro_industria = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'factura'


class Informe(models.Model):
    id_infome = models.IntegerField(primary_key=True)
    fecha_informe = models.DateField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')
    id_contenedor = models.IntegerField()
    invent_conts_id_contenedor = models.OneToOneField('InventarioContenedores', models.DO_NOTHING, db_column='invent_conts_id_contenedor')

    class Meta:
        managed = False
        db_table = 'informe'


class IngresoMaterial(models.Model):
    id_material = models.IntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=1)
    fecha = models.DateTimeField()
    pesos_material = models.IntegerField()
    llen_conts_id_llenado = models.OneToOneField('LlenadoContenedores', models.DO_NOTHING, db_column='llen_conts_id_llenado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso_material'


class InventarioContenedores(models.Model):
    id_contenedor = models.IntegerField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=1)
    peso = models.IntegerField()
    id_llenado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario_contenedores'


class LlenadoContenedores(models.Model):
    id_llenado = models.IntegerField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=1)
    peso = models.IntegerField()
    estado_contenedor = models.CharField(max_length=10)
    precio = models.IntegerField()
    invt_conts_id_contenedor = models.OneToOneField(InventarioContenedores, models.DO_NOTHING, db_column='invt_conts_id_contenedor')
    ingreso_material_id_material = models.OneToOneField(IngresoMaterial, models.DO_NOTHING, db_column='ingreso_material_id_material', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'llenado_contenedores'


class Precios(models.Model):
    id_precio = models.IntegerField(primary_key=True)
    tipo_material = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=20)
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'precios'


class Receptor(models.Model):
    rut_receptor = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    turno = models.DateTimeField()
    ingreso_material_id_material = models.OneToOneField(IngresoMaterial, models.DO_NOTHING, db_column='ingreso_material_id_material')

    class Meta:
        managed = False
        db_table = 'receptor'


class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    fecha_limite = models.DateField()
    venta_id_venta = models.OneToOneField(Compra, models.DO_NOTHING, db_column='venta_id_venta')
    comprador_id_comprador = models.ForeignKey(Comprador, models.DO_NOTHING, db_column='comprador_id_comprador')

    class Meta:
        managed = False
        db_table = 'reserva'


class Retiro(models.Model):
    id_retiro = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    fecha_retiro = models.DateField()
    contacto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'retiro'
