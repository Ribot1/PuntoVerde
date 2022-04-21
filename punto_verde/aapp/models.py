# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre = models.CharField(max_length=100)
    forma_pago = models.CharField(max_length=100)

    class Meta:
        db_table = 'boleta'


class Comprador(models.Model):
    id_comprador = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=100)

    class Meta:
        db_table = 'comprador'


class Contenedor(models.Model):
    id_contenedor = models.BigIntegerField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=1)
    peso = models.BigIntegerField()
    estado_contenedor = models.CharField(max_length=10)
    precio = models.BigIntegerField()

    class Meta:
        db_table = 'contenedor'


class ContenedorLleno(models.Model):
    id_cont = models.IntegerField(primary_key=True)
    reservado = models.FloatField()
    lleno = models.FloatField()
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva', blank=True, null=True)
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')

    class Meta:
        db_table = 'contenedor_lleno'


class DetaAsignacion(models.Model):
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')
    receptor_rut_receptor = models.ForeignKey('Receptor', models.DO_NOTHING, db_column='receptor_rut_receptor')

    class Meta:
        db_table = 'deta_asignacion'


class DetalleConte(models.Model):
    informe_id_infome = models.ForeignKey('Informe', models.DO_NOTHING, db_column='informe_id_infome')
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')

    class Meta:
        db_table = 'detalle_conte'


class Empleado(models.Model):
    rut_empleado = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.BigIntegerField()
    ocupacion = models.CharField(max_length=50)

    class Meta:
        db_table = 'empleado'


class Factura(models.Model):
    id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    giro_industria = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    class Meta:
        db_table = 'factura'


class Informe(models.Model):
    id_infome = models.BigIntegerField(primary_key=True)
    fecha_informe = models.DateField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')

    class Meta:
        db_table = 'informe'


class IngresoMaterial(models.Model):
    id_material = models.BigIntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=1)
    fecha = models.DateField()
    pesos_material = models.IntegerField()
    receptor_rut_receptor = models.ForeignKey('Receptor', models.DO_NOTHING, db_column='receptor_rut_receptor')
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')

    class Meta:
        db_table = 'ingreso_material'


class Receptor(models.Model):
    rut_receptor = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    turno = models.DateTimeField()

    class Meta:
        db_table = 'receptor'


class Reserva(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    fecha_limite = models.DateField()
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    comprador_id_comprador = models.ForeignKey(Comprador, models.DO_NOTHING, db_column='comprador_id_comprador')

    class Meta:
        db_table = 'reserva'


class Retiro(models.Model):
    id_retiro = models.BigIntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    fecha_retiro = models.DateField()
    contacto = models.BigIntegerField()

    class Meta:
        db_table = 'retiro'


class Venta(models.Model):
    id_venta = models.BigIntegerField(primary_key=True)
    monto = models.BigIntegerField()
    forma_pago = models.CharField(max_length=10)
    fecha_venta = models.DateField()
    reserva_id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='reserva_id_reserva')
    retiro_id_retiro = models.ForeignKey(Retiro, models.DO_NOTHING, db_column='retiro_id_retiro')
    emitido_en = models.CharField(max_length=30)

    class Meta:
        db_table = 'venta'
