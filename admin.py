from django.contrib import admin
from .models import *
from django import forms
from .forms import *
from django.urls import path
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from xhtml2pdf import pisa
import csv
from io import StringIO
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .forms import *
from django.urls import path
import csv
from io import StringIO
from simple_history.admin import SimpleHistoryAdmin
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
#Ultimo Cambio

@admin.register(Clientes)
class ClientesAdmin(SimpleHistoryAdmin):
    list_display = ('id','nombre_cliente', 'apellido_cliente', 'tipo_documento', 'documento', 'telefono', 'correo', 'rtn', 'direccion')
    search_fields = ['nombre_cliente', 'apellido_cliente', 'documento', 'telefono', 'correo', 'rtn', 'direccion']

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    search_fields = ('id' , 'nombre',)
    
@admin.register(MetodosPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    search_fields = ('id' , 'nombre',)
    
@admin.register(TipoCargo)
class TipoCargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    search_fields = ('id', 'nombre',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria', 'estado')
    search_fields = ('id', 'nombre_categoria', 'estado')
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_proveedor', 'telefono', 'correo', 'direccion', 'rtn', 'nombre_contacto', 'celular_contacto')
    search_fields = ('id', 'nombre_proveedor', 'telefono', 'correo', 'direccion', 'rtn', 'nombre_contacto', 'celular_contacto')

@admin.register(Descuento)
class DescuentoAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'nombre_descuento', 'descripción', 'valor_descuento', 'fecha_creación')
    search_fields = ('id', 'nombre_descuento', 'descripción', 'valor_descuento', 'fecha_creación')

#lleva el histico impuesto
@admin.register(Impuesto)
class ImpuestoAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'nombre_impuesto', 'descripción', 'valor_impuesto', 'fecha_creación')
    search_fields = ('id', 'nombre_impuesto', 'descripción', 'valor_impuesto', 'fecha_creación')


#lleva historico
@admin.register(Producto)
class ProductoAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'nombre_producto', 'descripcion', 'precio_venta', 'categoria', 'proveedor', 'estado', 'fecha_creacion')
    search_fields = ('id', 'nombre_producto', 'descripcion', 'precio_venta', 'categoria', 'proveedor', 'estado', 'fecha_creacion')


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'fecha_vencimiento', 'cantidad', 'Stock_minimo', 'Stock_maximo')
    search_fields = ('id', 'producto', 'fecha_vencimiento', 'cantidad', 'Stock_minimo', 'Stock_maximo')



@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_sucursal', 'ciudad', 'direccion', 'telefono', 'rtn', 'fecha_creacion')
    search_fields = ('id', 'nombre_sucursal', 'ciudad', 'direccion', 'telefono', 'rtn', 'fecha_creacion')


@admin.register(Empleados)
class EmpleadosAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'tipo_documento', 'documento', 'nombre_empleado', 'apellido_empleado', 'fecha_nacimiento', 'telefono', 'correo', 'tipo_cargo', 'sucursal', 'fecha_creacion')
    search_fields = ('id', 'tipo_documento', 'documento', 'nombre_empleado', 'apellido_empleado', 'fecha_nacimiento', 'telefono', 'correo', 'tipo_cargo', 'sucursal', 'fecha_creacion')


@admin.register(ComprasEncabezado)
class ComprasEncabezadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'no_factura', 'fecha_compra', 'observacion')
    search_fields = ('id', 'proveedor', 'no_factura', 'fecha_compra', 'observacion')


@admin.register(ComprasDetalle)
class ComprasDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'compra', 'producto', 'cantidad', 'precio_compra', 'sub_total', 'descuento', 'total')
    search_fields = ('id', 'compra', 'producto', 'cantidad', 'precio_compra', 'sub_total', 'descuento', 'total')


@admin.register(ParametroSar)
class ParametroSarAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_inicio', 'numero_fin')
    search_fields = ('id', 'numero_inicio', 'numero_fin')



@admin.register(FacturaParametro)
class FacturaEncabezadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa','parametros', 'fecha_emision', 'cai', 'fecha_creacion')
    search_fields = ('id', 'empresa','parametros', 'fecha_emision', 'cai', 'fecha_creacion')


class DetalleVentaForm(admin.TabularInline):
    model = DetalleVenta
    can_delete = True
    extra = 1
    autocomplete_fields=['producto']
    form = DetalleVentaForm


@admin.register(FacturaDet)
class FacturaDetAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaForm,]
    list_display = ('id', 'sub_total', 'descuento', 'impuesto', 'total')
    




@admin.register(Rutas)
class RutasAdmin(admin.ModelAdmin):
    list_display = ('id', 'ruta',)
    search_fields = ('id', 'ruta',)



@admin.register(Transporte)
class TransporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'ruta', 'nombre_carro', 'codigo', 'chofer')
    search_fields = ('id', 'ruta', 'nombre_carro', 'codigo', 'chofer')



@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id', 'carro', 'fecha_entrega', 'hora_entrega', 'direccion_entrega')
    search_fields = ('id', 'carro', 'fecha_entrega', 'hora_entrega', 'direccion_entrega')

@admin.register(Devoluciones)
class DevolucionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_producto', 'cantidad', 'descripcion', 'fecha_devolucion')
    search_fields = ('id', 'id_producto', 'cantidad', 'descripcion', 'fecha_devolucion')

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_cliente', 'id_producto', 'fecha_cotizacion')
    search_fields = ('id', 'id_cliente', 'id_producto', 'fecha_cotizacion')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_clientes', 'id_producto', 'fecha_pedido', 'total_pedido')
    search_fields = ('id', 'id_clientes', 'id_producto', 'fecha_pedido', 'total_pedido')
    
    

@admin.register(Factura)
class FacturaResource(resources.ModelResource):
    class Meta:
        model = Factura
    
def get_context_data(factura):
    detalles_libros = DetalleVenta.objects.filter(detalle=factura.detalle.id)
    
    datos_factura = {
        'encabezado': {
            'Sucursal': factura.Sucursal,
            'Dirección': factura.direccionSu,
            'numeroFactura': factura.numeroFactura,
            'fechaPago': factura.fechaPago,
            'horaFactura': factura.horaFactura,
            'idCliente': factura.idCliente,
            'cai': factura.idParametros.cai,
            'rtn': factura.rtn,
            'documento': factura.idCliente.documento,
        },
        'factura': factura.factura.all(),
        'detalles': factura.detallefactura_set.all(),
        'detalles_libros': detalles_libros,
    }

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('consecutivo', 'empleado', 'cliente', 'tipo_pago', 'tarjeta', 'efectivo', 'hora', 'fecha_creacion')
    search_fields = ('consecutivo','cliente','empleado')
    readonly_fields = ('consecutivo',)

    def boton_pdf(self, obj):
        # Get the context data
        context_data = self.get_context_data(obj)

        # Render the template
        template = get_template('factura.html')
        html = template.render(context_data)

        # Create a PDF file using xhtml2pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={obj.consecutivo}.pdf'

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response

    boton_pdf.short_description = 'PDF Factura'

    def get_context_data(self, obj):

        detalles_libros = DetalleVenta.objects.filter(detalle=obj.id)
        
        context = {
            'encabezado': {
                'Sucursal': obj.Sucursal,
                'Dirección': obj.direccionSu,
                'numeroFactura': obj.numeroFactura,
                #'rtn': obj.rtn,
                'fechaPago': obj.fechaPago,
                'horaFactura': obj.horaFactura,
                'idCliente': obj.idCliente,
                'cai': obj.idParametros.cai,
                'rtn':obj.rtn,
                'documento': obj.idCliente.documento,

            },
            'factura': obj.factura.all(),
            'detalles': obj.detallefactura_set.all(),
            'detalles_libros': detalles_libros,

        }
        return context
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
      formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
      if db_field.name == 'numero_factura':
         errors = formfield.error_messages.copy()
         errors['rango_final'] = 'Advertencia: Se ha alcanzado el rango final de facturación.'
         formfield.error_messages = errors
         return formfield
